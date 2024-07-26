#!/usr/bin/env python
import httpx
import asyncio
from bs4 import BeautifulSoup
import time

async def download(queue_download:asyncio.Queue,queue_save:asyncio.Queue):
    while True:
        url = await queue_download.get()
        log_file = url.split('/')[-1]
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            msg ={
                "log_file":log_file,
                "text":response.text
            }
            queue_save.put_nowait(msg)
        queue_download.task_done()


async def save(queue_save:asyncio.Queue):
    while True:
        data = await queue_save.get()
        log_file = data['log_file']
        text = data['text']
        with open(log_file,"w") as f:
            f.write(text)

        queue_save.task_done()


async def main():
    start = time.perf_counter()

    queue_download = asyncio.Queue()
    queue_save = asyncio.Queue()
    nb_download_workers = 10
    nb_save_workers = 5

    url = "https://logs.eolem.com/"
    response = httpx.get(url) # ,verify=False disable ssl verif
    soup = BeautifulSoup(response.text, 'html.parser')

    all_files = [url+a['href'] for a in soup.find_all('a') if "apache_logs_" in a['href']]
    tasks = []
    
    for i in range(nb_download_workers):
        task = asyncio.create_task(download(queue_download,queue_save))
        tasks.append(task)

    for i in range(nb_save_workers):
        task = asyncio.create_task(save(queue_save))
        tasks.append(task)


    for url in all_files:
        queue_download.put_nowait(url)

    await queue_download.join()
    await queue_save.join()
    
    # Stop all workers
    [task.cancel() for task in tasks]
    end = time.perf_counter()
    print(f"{end-start:.3}s")
    

if __name__ == '__main__':
    asyncio.run(main())
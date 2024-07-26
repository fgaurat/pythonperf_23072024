#!/usr/bin/env python
import httpx
import asyncio
from bs4 import BeautifulSoup

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
    queue_download = asyncio.Queue()
    queue_save = asyncio.Queue()
    nb_download_workers = 10
    nb_save_workers = 5

    url = "https://logs.eolem.com/"
    response = httpx.get(url) # ,verify=False disable ssl verif
    soup = BeautifulSoup(response.text, 'html.parser')

    all_files = [url+a['href'] for a in soup.find_all('a') if "apache_logs_" in a['href']]
    print(all_files)

if __name__ == '__main__':
    asyncio.run(main())
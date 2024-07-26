#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import time
import asyncio
from functools import partial
import httpx


async def download(url,log_file):
    # response =  await requests.get(url) FAUX
    response =  requests.get(url)
    with open(log_file,"w") as f:
        f.write(response.text)

async def download_requests(url_log,log_file):
    loop = asyncio.get_event_loop()
    # response = await loop.run_in_executor(None, requests.get, url_log)
    get_with_verify_false = partial(requests.get, verify=False)

    response = await loop.run_in_executor(None, get_with_verify_false, url_log)

    with open(log_file,'w') as f:
        f.write(response.text)

async def download_httpx(url_log,log_file):
    async with httpx.AsyncClient() as client:
        response = await client.get(url_log)

    with open(log_file,'w') as f:
        f.write(response.text)


async def main():
    start = time.perf_counter()
    url = "https://logs.eolem.com/"
    response = requests.get(url) # ,verify=False disable ssl verif
    soup = BeautifulSoup(response.text, 'html.parser')

    all_files = [a['href'] for a in soup.find_all('a') if "apache_logs_" in a['href']]

    tasks =[]
    for file_name in all_files:
        url_file = f"{url}{file_name}"
        # tasks.append(download_requests(url_file,file_name))
        tasks.append(download_httpx(url_file,file_name))

    await asyncio.gather(*tasks)


    end = time.perf_counter()
    print(f"{end-start:.3}s")

if __name__ == '__main__':
    asyncio.run(main())
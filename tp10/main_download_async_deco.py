#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import time
import asyncio
from functools import partial
import requests

def make_async(func):
    
    async def wrapper(*args, **kwargs):
        
        return await asyncio.to_thread(func, *args, **kwargs)
    
    return wrapper

@make_async
def download(url,log_file):
    response = requests.get(url)
    with open(log_file,"w") as f:
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
        tasks.append(download(url_file,file_name))

    await asyncio.gather(*tasks)


    end = time.perf_counter()
    print(f"{end-start:.3}s")

if __name__ == '__main__':
    asyncio.run(main())
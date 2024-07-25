#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import time
import threading

def download(url,log_file):
    response = requests.get(url)
    with open(log_file,"w") as f:
        f.write(response.text)

def main():
    start = time.perf_counter()
    url = "https://logs.eolem.com/"
    response = requests.get(url) # ,verify=False disable ssl verif
    soup = BeautifulSoup(response.text, 'html.parser')

    all_files = [a['href'] for a in soup.find_all('a') if "apache_logs_" in a['href']]
    all_threads = []
    for file_name in all_files:
        url_file = f"{url}{file_name}"
        th = threading.Thread(target=download,args=(url_file,file_name))
        th.start()
        all_threads.append(th)

    [t.join() for t in all_threads]
    end = time.perf_counter()
    print(f"{end-start:.3}s")

if __name__ == '__main__':
    main()
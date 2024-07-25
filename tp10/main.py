#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import time

def main():
    start = time.perf_counter()
    url = "https://logs.eolem.com/"
    response = requests.get(url) # ,verify=False disable ssl verif
    soup = BeautifulSoup(response.text, 'html.parser')

    all_files = [a['href'] for a in soup.find_all('a') if "apache_logs_" in a['href']]

    for file_name in all_files:
        url_file = f"{url}{file_name}"
        response = requests.get(url_file)
        with open(file_name,"w") as f:
            f.write(response.text)

    end = time.perf_counter()
    print(f"{end-start:.3}s")
if __name__ == '__main__':
    main()
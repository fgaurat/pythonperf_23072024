#!/usr/bin/env python
import csv
from pprint import pprint
import sqlite3

def main():
    sql_insert = "INSERT INTO customers_tbl(first_name,last_name,email,gender,ip_address) VALUES(?,?,?,?,?)"

    with sqlite3.connect("./tp09/customers_db.db") as con:

        with open(r'./tp09/MOCK_DATA.csv') as f:
            reader = csv.DictReader(f)
            for data in reader:
                del data['id']
                con.execute(sql_insert,list(data.values()))



if __name__ == '__main__':
    main()
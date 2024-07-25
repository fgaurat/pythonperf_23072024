import sqlite3
from Customer import Customer

class CustomerDAO:


    def __init__(self,db_file):
        self.con = sqlite3.connect(db_file)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.con:
            if exc_type is None:
                self.con.commit()
            else:
                self.con.rollback()
            self.con.close()

    
    def findAll(self):
        sql = "SELECT id,first_name,last_name,email,gender,ip_address FROM customers_tbl"
        cur = self.con.cursor()
        rs = cur.execute(sql)
        for row in rs:
            c = Customer(*row)
            yield c

    def save(self,customer):
        sql = """INSERT INTO customers_tbl(first_name,last_name,email,gender,ip_address) 
        VALUES (?,?,?,?,?)"""
        cur = self.__con.cursor()
        d = customer.__dict__
        del d["id"]
        cur.execute(sql,list(d.values()))
        self.__con.commit()

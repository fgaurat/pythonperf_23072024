#!/usr/bin/env python
from CustomerDAO import CustomerDAO
def main():
    # dao = CustomerDAO("./tp09/customers_db.db")
    with CustomerDAO("./tp09/customers_db.db") as dao:
        customers = dao.findAll()
        for customer in customers:
            print(customer)

        # for customer in customers:
        #     print(customer.name)
        #     print(customer.firstName)

if __name__ == '__main__':
    main()
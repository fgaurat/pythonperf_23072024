#!/usr/bin/env python

def make_incrementor(inc_value):

    def f(value):
        return value+inc_value

    return f



def main():
    # Function builder
    do_inc = make_incrementor(2)
    do_inc_10 = make_incrementor(10)
    
    r = do_inc(1)
    print(r)# 3

    r = do_inc(6)
    print(r)# 8

    r = do_inc(12)
    print(r)# 14
    
    r = do_inc_10(12)
    print(r)# 22

if __name__ == '__main__':
    main()
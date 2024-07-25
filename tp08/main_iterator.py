#!/usr/bin/env python
import time

class CompteARebours:

    def __init__(self,start) -> None:
        self.value = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.value<0:
            raise StopIteration
        current_value = self.value
        self.value-=1
        return current_value

def compte_a_rebours(n):
    while n>0:
        # time.sleep(1)
        print("compte_a_rebours",n)
        yield n
        n-=1


def filtre_pairs(generateur):
    for i in generateur:
        if i%2 ==0:
            yield i

def main():
    # c = CompteARebours(5)
    # v1 = next(c)
    # print(v1)
    # for i in c:
    #     print(i)

    c = compte_a_rebours(5) # compte_a_rebours | filtre_pairs
    # p = filtre_pairs(c)
    # # p = filtre_pairs(compte_a_rebours(5))
    # print(type(c))
    # for i in p:
    #     print(i)

    # l = list(c)
    for i in c:
        print('loop',i)
        print(50*'-')
    for i in c:
        print('loop',i)
if __name__ == '__main__':
    main()
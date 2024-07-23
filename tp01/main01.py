import sys

def main():
    a = 2
    b = 2
    print(a,hex(id(a)))
    print(b,hex(id(b)))
    b = 3
    print(a,hex(id(a)))
    print(b,hex(id(b)))

    print("getrefcount",sys.getrefcount(456723456754))
    c = 456723456754
    print("getrefcount",sys.getrefcount(456723456754))
    d = 456723456754
    print("getrefcount",sys.getrefcount(456723456754))
    print(c,hex(id(c)))
    print(d,hex(id(d)))
    print("getrefcount",sys.getrefcount(2))

if __name__ == '__main__':
    main()
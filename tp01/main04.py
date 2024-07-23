from collections import deque

def main():
    l = [10,20,30,40,50]
    print(l)
    l.append(60)
    print(l)
    last_value = l.pop()
    print(last_value)
    print(l)
    l.insert(0,5)
    print(l)
    first_value = l.pop(0)
    print(first_value)
    print(l)
    
    
    d = deque(l) # decorator
    print(d)
    d.appendleft(2)
    print(d)
    first_value = d.popleft()
    print(first_value,d)


if __name__ == '__main__':
    main()
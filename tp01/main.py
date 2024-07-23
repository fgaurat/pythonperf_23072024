
def mult2(i):
    return i*2

def main():
    l = [10,20,30,40,50]
    
    l2 = []
    # Scolaire
    for i in l:
        l2.append(i*2)
    
    print(l)
    print(l2)

    # mult2 = lambda i:i*2
    # m = list(map(mult2,l))
    
    # Dev
    m = list(map(lambda i:i*2,l))
    print(m)

    # Comprehension de list
    l2 = [i*2 for i in l]
    print(l2)

    l3 = ["   toto","titi    ","   tata    "]
    print(l3)
    clean_l3 = [s.strip() for s in l3]
    print(clean_l3)
    l = [10,20,30,40,50]
    # l4 = [i for i in l] # map
    l4 = [i for i in l if i>20 and i<50]
    # l4 = []
    # for i in l:
    #     if i>20:
    #         l4.append(i)
    print(l4)



if __name__ == '__main__':
    main()
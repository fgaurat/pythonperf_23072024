import copy
def main():
    l = [10,20,30,40,50]
    print(l)
    l[0] = 1000
    print(l)
    print(l[-1])
    # slices
    s1 = l[2:4] # [2:3[
    print(s1)

    # l1 = l
    l1 = l[:]# copie du début à la fin
    l1 = l.copy()# copie via méthode
    l1 = copy.copy(l)# copie via fonction

    l[0]=12
    print("l",l) # [12,20,30,40,50]
    print("l1",l1)
                
    l2 = [
        [10,20,30],
        [40,50,60],
        [70,80,90],
    ]
    l3 = copy.deepcopy(l2)
    l2[1][1] = 0
    print(l2)
    print(l3)



if __name__ == '__main__':
    main()
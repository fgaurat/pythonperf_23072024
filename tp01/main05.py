
def add(*l):
    print(l)
    result  = 0
    for i in l:
        result+=i
    return result

# def hello(firstName,name):
def hello(**kwargs):

    print("Hello",kwargs['firstName'],kwargs['name'])

def main():
    l = [10,20,30,40,50]

    r = add(*l) 
    print(r) #150

    r = add(10,20,30,40,50) 
    print(r)

    l = [10,20,30,40]
    a,b,*c = l # ValueError: too many values to unpack (expected 3)
    print(a,b,c,l)
    # a,b,c,d,e = l # ValueError: not enough values to unpack (expected 5, got 4)
    a,*b,c = l
    print(a)
    print(b)
    print(c)

    t = 2

    hello(firstName="Fred",name="GAURAT")
    
    d = {
        "firstName":"Fred",
        "name":"GAURAT"
    }

    hello(**d) # hello(firstName="Fred",name="GAURAT")
    
    l = [10,20,30,40]
    
    s1 = "value01: {0} ,value02: {1} ".format(l[0],l[1])
    s1 = "value01: {0} ,value02: {1} ".format(*l)
    print(s1)
    s2 = "Bonjour {fname}, {lname}".format(fname = d['firstName'],lname=d['name'])
    s2 = "Bonjour {firstName}, {name}".format(**d)
    print(s2)

    s3 = f"Bonjour {d['firstName']=}, {d['name']=}" # interpolation de variable
    print(s3)

    s4 = "L'orage gronde"

if __name__ == '__main__':
    main()
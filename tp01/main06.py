
def main():
    l = [10,20,30,40,50]

    for i in l:
        print(i)
        if i>30:
            print("break")
            break # pas de else
    else:
        print("ok")

if __name__ == '__main__':
    main()
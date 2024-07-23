
a = 2

# UnboundLocalError => UpperCamelCase, PascalCase
# unboundLocalError => camelCase
# unbound_local_error => snake_case
# unbound-local-error => kebab-case

def main():
    global a
    print("main",a)
    a = 3
    print("main",a)
    # c = 3
    # print("main",c)
    # print("main",a)

if __name__ == '__main__':
    print("avant",a)
    main()
    print("après",a)
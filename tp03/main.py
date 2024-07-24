import traceback


def divi(a,b):
    return a/b

def call_divi(a,b):
    try:
        print('open log file')
        c = divi(a,b)
    finally:
        print('close log file')
    return c

def main():
    try:
        a = 2
        b = 0
        c = call_divi(a,b)
        print(c)

    except ZeroDivisionError as e:
        print("ZeroDivisionError",e,type(e))
        traceback.print_exc()
    except ValueError as e:
        print("ValueError",e,type(e))
        traceback.print_exc()
    except Exception as e: # Polymorphisme
        print("Exception",e,type(e))
        traceback.print_exc()
    else: # seulement si pas d'erreurs
        print("pas d'erreurs")
    finally:
        print("finally erreurs ou pas")
    
    print("la suite du code")

if __name__ == '__main__':
    main()
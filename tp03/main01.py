import traceback
def main():
    try:
        a = 2
        b = int(input("Valeur de b:"))
        c = a/b
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
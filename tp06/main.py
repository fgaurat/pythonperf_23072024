
class A:
    def show(self):
        print('A')

class B(A):
    def show(self):
        print('B')

class C(A):
    def show(self):
        print('C')

class D(C,B):
    
    def show(self):
        super().show() # show de C
        super(D,self).show() # show de C
        super(C,self).show() # show de B
        super(B,self).show() # show de A
        
        print('D')


def main():
    print(D.mro())
    d = D()
    d.show()

if __name__ == '__main__':
    main()
class A:


    def show(self):
        print('&quot')

class B(A):
    def show(self):
        print( )

class C(B):
            def show(self):
                print()

class D(C,B):
    pass

r = D()
r.show()
# inheritance with constructor

class A:
    def __init__(self, a,b):
        print("this is constructor from class A", a,b)

class B:
    def __init__(self, a,b):
        print("this is constructor from class B",a,b)

class C(A, B):
    def __init__(self, a,b,c,d,e,f):
        print("this is constructor from class C", a,b)
        # appr 1
        # A.__init__(self,c,d)
        # B.__init__(self,e,f)
        # super()
        super().__init__(a, b)


    def child_func(self):
        print("This is child func")
        print("#############same Func################")


obj= C(1,2,3,4,5,6)
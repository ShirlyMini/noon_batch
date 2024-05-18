#### types of inheritance
# single-->
# mutiple
#multilevel
#hirercheal
#hybrid

#################################################
# single

# class A:
#     def func1(self):
#         print("func1 from class A")
#
# class B(A):
#     def func2(self):
#         print("func2 from class B")
#
# obj= B()
# obj.func1()
# obj.func2()

##################################################33
#mutiple

# class A:
#     def func1(self):
#         print("func1 from class A")
#
# class B:
#     def func2(self):
#         print("func2 from class B")
#
# class C:
#     def func3(self):
#         print("func3 from class C")
#
# class D(A, B, C):
#     def func4(self):
#         print("func4 from class D")
#
# obj=D()
# obj.func1()
# obj.func2()
# obj.func3()
# obj.func4()

##################################################33
#multi level

# class A:
#     def func1(self):
#         print("func1 from class A")
#
# class B(A):
#     def func2(self):
#         print("func2 from class B")
#
# class C(B):
#     def func3(self):
#         print("func3 from class C")
#
# obj=C()
# obj.func1()
# obj.func2()
# obj.func3()

##################################################33
#hierarchial level

# class A:
#     def func1(self):
#         print("func1 from class A")
#
# class B(A):
#     def func2(self):
#         print("func2 from class B")
#
# class C(A):
#     def func3(self):
#         print("func3 from class C")
#
# objb=B()
# objb.func1()
# objb.func2()
#
# objc=C()
# objc.func1()
# objc.func3()

#######################################33
# hybrid

class A:
    def func1(self):
        print("func1 from class A")

class A1(A):
    def func4(self):
        print("func4 from class A1")

class A2(A1):
    def func5(self):
        print("func5 from class A2")

class B(A2):
    def func2(self):
        print("func2 from class B")

class C(A2):
    def func3(self):
        print("func3 from class C")

objb=B()
objb.func1()
objb.func2()
objb.func4()
objb.func5()
#
objc=C()
objc.func1()
objc.func3()
objc.func4()
objc.func5()
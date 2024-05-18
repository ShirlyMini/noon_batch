# single

# class A:
#     var="class A var"
#     var1="class A var1"
#     def func1(self):
#         print("func1 from class A")
#
# class B(A):
#     var = "class B var"
#     def func1(self):
#         print("func1 from class B")
#     def child_func(self):
#         print("#############child Func################")
#         print("#############same variable################")
#         print(self.var)
#         print(self.var1)
#         print(A.var)
#         print("#############same Func################")
#         self.func1()
#         A.func1(self)
#
#
# obj= B()
# obj.child_func()

#######################
#multiple inheritace

# class A:
#     var="class A var"
#     var1="class A var1"
#     def func1(self):
#         print("func1 from class A")
#
# class B:
#     var="class B var"
#     var2="class B var2"
#     def func1(self):
#         print("func1 from class B")
#
# class C(B, A):# method resolution order # com var preset in child(pro=1)# B(pro=2)# A(Pro-=3)
#     var = "class C var"
#     var3 = "class C var3"
#
#     def func1(self):
#         print("func1 from class C")
#
#     def child_func(self):
#         print("This is child func")
#         print("#############same variable################")
#         print(self.var)
#         print(self.var1)
#         print(self.var2)
#         print(self.var3)
#         print(A.var)
#         print(B.var)
#         print("#############same Func################")
#         self.func1()
#         A.func1(self)
#         B.func1(self)
#         # self.child_func()#RecursionError: maximum recursion depth exceeded while calling a Python object
#
#
# obj= C()
# obj.child_func()


# class A:
#     @classmethod
#     def func1(cls):
#         print("func1 from class A")
#
# class B:
#     @classmethod
#     def func1(cls):
#         print("func1 from class B")
#
# class C(B, A):
#     @classmethod
#     def func1(cls):
#         print("func1 from class C")
#
#     def child_func(self):
#         print("This is child func")
#         print("#############same Func################")
#         self.func1()
#         A.func1()
#         B.func1()
#
#     @classmethod
#     def child_clsmthod(cls):
#         print("This is child func")
#         print("#############same Func################")
#         cls.func1()
#         A.func1()
#         B.func1()
#
#
#
#
# obj= C()
# # obj.child_func()
# obj.child_clsmthod()

class A:
    @staticmethod
    def func1():
        print("func1 from class A")

class B:
    @staticmethod
    def func1():
        print("func1 from class B")

class C(B, A):
    @staticmethod
    def func1():
        print("func1 from class C")

    def child_func(self):
        print("This is child func")
        print("#############same Func################")
        self.func1()
        A.func1()
        B.func1()

    @classmethod
    def child_clsmthod(cls):
        print("This is child func")
        print("#############same Func################")
        cls.func1()
        A.func1()
        B.func1()

    @staticmethod
    def child_staticmthod():
        print("This is child func")
        print("#############same Func################")
        C.func1()
        A.func1()
        B.func1()




obj= C()
# obj.child_func()
# obj.child_clsmthod()
obj.child_staticmthod()



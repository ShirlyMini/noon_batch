# global/local/class/instance
# global/local/class
###################################################
# instance method
###################################################
var1="global var"

class myclass:
    var2="class var"

    def func1(self):# instance method
        var3="local var"
        self.var4="local var convrted to class var"
        print(f'global variable : ', var1)
        print(f'class variable using self : ', self.var2)# standard
        print(f'class variable using myclass : ', myclass.var2)
        print(f'local variable : ', var3)
        return var3

    def func2(self):
        print(self.var4)

obj=myclass()
obj.func1()
# print("################outside class")
# print(obj.var2)
# print(myclass.var2)
# obj.var2="class var changed"
# myclass.var2="class var changed 123"
# print(var1)
# print(obj.var2)
# print(myclass.var2)
# loacl_var = obj.func1()
# print(loacl_var)


#############################################################

# var="global var"

# class myclass:
#     var="class var"
#
#     def func1(self):# instance method
#         var="local var"
#         print(f'global variable : ', globals()['var'])
#         print(f'class variable using self : ', self.var)# standard
#         print(f'class variable using myclass : ', myclass.var)
#         print(f'local variable : ', var)
#         return var
#
# obj=myclass()
# obj.func1()
# ############################outside class
# print("################outside class")
# print(obj.var)
# print(myclass.var)
# obj.var="class var changed using obj"
# myclass.var="class var changed using myclass"
# print(var)
# print(obj.var)
# print(myclass.var)
# loacl_var = obj.func1()
# print(loacl_var)

###################################################
# class method
###################################################

# var1="global var"
#
# class myclass:
#     var2="class var"
#
#     @classmethod
#     def func1(cls):# class method
#         var3="local var"
#         print(f'global variable : ', var1)
#         print(f'class variable using cls : ', cls.var2)# standard
#         print(f'class variable using myclass : ', myclass.var2)
#         print(f'local variable : ', var3)
#         return var3
#
# obj=myclass()
# obj.func1()
# print("################outside class")
# print(obj.var2)
# print(myclass.var2)
# obj.var2="class var changed"
# myclass.var2="class var changed 123"
# print(obj.var2)
# print(myclass.var2)
# loacl_var = obj.func1()
# print(loacl_var)
# print(var1)

# var="global var"
#
# class myclass:
#     var="class var"
#
#     @classmethod
#     def func1(cls):# class method
#         var="local var"
#         print(f'global variable : ', globals()['var'])
#         print(f'class variable using cls : ', cls.var)# standard
#         print(f'class variable using myclass : ', myclass.var)
#         print(f'local variable : ', var)
#         return var
#
# obj=myclass()
# obj.func1()
# print("################outside class")
# print(obj.var)
# print(myclass.var)
# obj.var="class var changed"
# myclass.var="class var changed 123"
# print(obj.var)
# print(myclass.var)
# loacl_var = obj.func1()
# print(loacl_var)
# print(var)

###################################################
# static method
###################################################

# var1="global var"
#
# class myclass:
#     var2="class var"
#
#     @staticmethod
#     def func1():# static method
#         var3="local var"
#         print(f'global variable : ', var1)
#         print(f'class variable using myclass : ', myclass.var2)
#         print(f'local variable : ', var3)
#         return var3
#
# obj=myclass()
# obj.func1()
# print("################outside class")
# print(obj.var2)
# print(myclass.var2)
# obj.var2="class var changed"
# myclass.var2="class var changed 123"
# print(obj.var2)
# print(myclass.var2)
# loacl_var = obj.func1()
# print(loacl_var)
# print(var1)

var="global var"

class myclass:
    var="class var"

    @staticmethod
    def func1():# static method
        var="local var"
        print(f'global variable : ', globals()['var'])
        print(f'class variable using myclass : ', myclass.var)
        print(f'local variable : ', var)
        return var

obj=myclass()
obj.func1()
print("################outside class")
print(obj.var)
print(myclass.var)
obj.var="class var changed"
myclass.var="class var changed 123"
print(obj.var)
print(myclass.var)
loacl_var = obj.func1()
print(loacl_var)
print(var)
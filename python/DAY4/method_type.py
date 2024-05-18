# instance method(default)
# class method
# static method

class myclass:
    def func1(self, a,b):
        print(self)#<__main__.myclass object at 0x000001B6831C4150>
        print("this is instance method func1",a,b)

obj1=myclass()
print(obj1)
obj1.func1(10,20)# passes obj as first parameter



# obj1 = myclass
# print(obj1)
# obj1.func1(10,20,30)


##########################################################3
# class method
########################################################

# class myclass:
#     @classmethod
#     def func1(cls,a,b):
#         print(cls)#<class '__main__.myclass'>
#         print("this is class method func1",a,b)

# obj1=myclass()
# print(obj1)
# obj1.func1(1,2)# class name passed as first parameter

# obj1=myclass
# print(obj1)
# obj1.func1()# class name passed as first parameter
#
# or

# myclass.func1(1,2)


##########################################################3
# static method
##########################################################3

# class myclass:
#     @staticmethod
#     def func1(a, b):
#         print("this is static method", a,b)
#
# obj1=myclass()
# obj1.func1(1,2)
#
# obj1=myclass
# obj1.func1(1,2)


###########################################################3
# instance method-default method-self parameter as first parameter(self== obj)---access using object/createion
# class method -@classmethod-cls parameter ad first(cls==classname)-- access using class name
# static method - @staticmethod - no parameter-- access uing class name
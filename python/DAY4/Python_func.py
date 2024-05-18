# set of statements
# def is keyword and return

# def myfunc():
#     print("this is my function")
#
# # myfunc()# invoke the function
# print(myfunc)# ref of function # namespace
# var=myfunc
# var()

##############################3
# with parameter and without return
# without parameter and without return
# with parameter and with return
# without parameter and with return

# def myfunc():
#     # print("this/ is myfunction")
#     # return
#
# # var = myfunc()
# # print(var)
# # or
# print(myfunc())

# empty function or do nothing function
# def myfunc():
#     pass
#
# myfunc()

# def addition():
#     a=3
#     b=4
#     c=a+b
#     return a,b,c
#
# tup = addition()
# print(tup[0])
# print(tup[1])
# print(tup[2])

####################################3parameters

# positional
# def addition(a,b,c,d):
#     print(f"a:{a} b:{b} c:{c} d:{d} = {a+b+c+d}")
#
# addition(1,2,3,4)#a:1 b:2 c:3 d:4 = 10
# addition(1,2,13,4)#a:1 b:2 c:3 d:4 = 10
# addition(1,2,4,3)#a:1 b:2 c:3 d:4 = 10
# # addition(1,2,3)#TypeError: addition() missing 1 required positional argument: 'd'
# # addition(1)#TypeError: addition() missing 3 required positional arguments: 'b', 'c', and 'd'

# def addition(a,b,c=0,d=0):
#     print(f"a:{a} b:{b} c:{c} d:{d} = {a+b+c+d}")
# addition(1,2,3,4)
# addition(1,2)


# Rule1=SyntaxError: non-default argument follows default argument

# keyword
# def addition(a,b,c,d):
#     print(f"a:{a} b:{b} c:{c} d:{d} = {a+b+c+d}")
#
# addition(a=1,b=2,c=3,d=4)
# addition(c=3,d=4,a=1,b=2)
# # addition(c=3,d=4)#TypeError: addition() missing 2 required positional arguments: 'a' and 'b'

# def addition(a,b,c=0,d=0):
#     print(f"a:{a} b:{b} c:{c} d:{d} = {a+b+c+d}")

# addition(a=1,b=2,c=3,d=4)
# addition(c=3,d=4,a=1,b=2)
# addition(a=1,b=2)
# addition(a=1)#TypeError: addition() missing 1 required positional argument: 'b'

# addition(1,2,c=10,d=20)
# addition(1,2,a=10,b=20)#TypeError: addition() got multiple values for argument 'a'
# addition(a=1,b=2,10,20)#SyntaxError: positional argument follows keyword argument


##################################
# variable scope

# global and local (fucn)

# ex 1
# x="gloabl var"
#
# def myfunc():
#     y="local var"
#     print(f"gloabl{x} : local{y} inside myfunc")

# print(f"gloabl{x} : local{y} before calling myfunc ")#NameError: name 'y' is not defined
# myfunc()
# print(f"gloabl{x} : local{y} after calling myfunc ")#NameError: name 'y' is not defined


# ex2

# a="global var"
#
# def myfunc():
#     a="local var"
#     print(f"global{a} : local{a} inside myfunc")
#
# print(f"global {a} : local {a} before calling myfunc ")
# myfunc()
# print(f"global {a} : local {a} after calling myfunc ")

#ex3

# a = "global var"
#
#
# def myfunc():
#     global a
#     a = "local var"
#     print(f"global{a} : local{a} inside myfunc")
#
#
# print(f"global {a} : local {a} before calling myfunc ")
# myfunc()
# print(f"global {a} : local {a} after calling myfunc ")
# print(f"global {a} : local {a} after calling myfunc ")
# print(f"global {a} : local {a} after calling myfunc ")

# ex4

# a = "global var"
#
#
# def myfunc():
#     a = "local var"
#     global a#SyntaxError: name 'a' is assigned to before global declaration
#     print(f"global{a} : local{a} inside myfunc")
#
#
# print(f"global {a} : local {a} before calling myfunc ")
# myfunc()
# print(f"global {a} : local {a} after calling myfunc ")

# ex5
#
# x="gloabl var"
#
# def myfunc():
#     global y
#     y="local var"
#     print(f"gloabl{x} : local{y} inside myfunc")
#
# # print(f"gloabl{x} : local{y} before calling myfunc ")#NameError: name 'y' is not defined
# myfunc()
# print(f"gloabl{x} : local{y} after calling myfunc ")#gloablgloabl var : locallocal var after calling myfunc

# ex6
# a = "global var"
#
#
# def myfunc(b,c):
#     global a
#     # global b#SyntaxError: name 'b' is parameter and global
#     # global c#SyntaxError: name 'b' is parameter and global
#     a = "local var"
#     # global a#SyntaxError: name 'a' is assigned to before global declaration
#     print(f"global{a} : local{a} inside myfunc")
#
#
# print(f"global {a} : local {a} before calling myfunc ")
# myfunc(10,20)
# print(f"global {a} : local {a} after calling myfunc ")


#################################
# *args and **kwargs

# def myfunc(*args):
#     print(args)
#     sum=0
#     for i in args:
#         sum=sum+i
#
#     print(sum)
#
# myfunc(1,2,3)
# myfunc(1,2,3,4,5,6,7)
# myfunc(1,2,3,4,5,6,7,8,9,10)

def myfunc(**kwargs):
    print(kwargs)#dict
    sum=0
    for i in kwargs.values():
        sum=sum+i

    print(sum)

myfunc(a=1,b=2,c=3)
myfunc(a=1,b=2,c=3,d=4,e=5,f=6,g=7)
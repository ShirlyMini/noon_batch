# taking more than one form is poly
# overload and override
# overload

# operator overload

#+ *
# print(10+10)
# print("string"+"string")
#
# print(10*10)
# print("string"*10)
# print(["string"]*10)

# method overload
# def addition(*args):
#     print(*args)
#
# addition(1,2)
# addition(1,2,3)
# addition(1,2,3,4,5)

# method override-****NA in python

def addition(a):
    print("1st", a)

def addition(a):
    print("2nd", a)

def addition(a):
    print("3rd", a)

# addition(1)

class myclass:
    def addition(a):
        print("1st", a)

    def addition(a):
        print("2nd", a)

    def addition(a):
        print("3rd", a)

obj=myclass()
obj.addition()
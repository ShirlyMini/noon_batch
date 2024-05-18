# syntax error- indendation

# exception- type error, name, value

#try and except

# print("program1")
# print("program2")
# try:
#     print(a)#NameError: name 'a' is not defined
# except:
#     print("error happend!!!")
# print("program3")
# print("program4")


list1=[1,2,3,4]
try:
    # print(a)#NameError: name 'a' is not defined
    # print(10+"string")# typeerror
    # print(list1[5])# indexERROR
    print(1/0)

except NameError as msg:
    print("Name ERROR happened", msg)
except IndexError as msg:
    print("Index ERROR happened", msg)
except Exception as msg:
    print("error happend!!!", msg)

else:
    print("No exception happened")
finally:
    print("finally block")

# else and finally(option)
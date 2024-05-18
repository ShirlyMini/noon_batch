# raise(if condition)(custom error)
# raise SyntaxError("this is user raised exception")
# try:
#     n=2003
#     if n%4==0:
#         print("leap year")
#     else:
#         raise ImportError("not leap year")
# except Exception as msg:
#     print("Exception handled",msg)

# assert(condtion)(assertion error)
# assert True(Pass flag)
# assert False(Fail)
# assert 4>5, "4 is not greater than 5"

try:
    n=2003
    assert n%4==0, "Not Leap year"
    print(n,"leap year")
except Exception as msg:
    print("Exception handled",msg)
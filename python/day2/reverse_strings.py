# using slicing
# print(str1[::-1])# reverse string

# using for loop

# str1="welcome"
# rev_str=''
# for i in str1:
#     rev_str=i+rev_str# p+""=p
#                     #y+p=yp
#                     #t+yp=typ
#     print(rev_str)
# print(rev_str)

# using inbuild funct
# reversed
str1="welcome"
rev_str=''
print(list(reversed(str1)))

for i in list(reversed(str1)):
    rev_str=rev_str+i

print(rev_str)

# arry of bytes
# arry - coll of homogeneous data
# list - coll of heter

### create str
# str1="python"
# str2='python'
# str3=str('welcome')

# empty str

# str1=""
# str2=''
# str3=str()
# print(str3)

# slicing

str1="welcome"# 0 to n-1
#-4 -3 -2 -1 0 1 2 3 4 5
# print(str1[0])
# print(str1[1])
# print(str1[2])
# print(str1[3])
# print(str1[4])
# print(str1[5])
# print(str1[6])
# # print(str1[7])#IndexError: string index out of range

# #start=0:end=n-1:step=1
# print(str1[0:4])
# print(str1[:4])
# print(str1[3:])
# print(str1[2:8:1])
# print(str1[::2])
# print(str1[::3])

# w     e   l   c   o     m        e
# -7    -6- 5   -4- 3    -2         - 1

print(str1[-1])# prints last letter
print(str1[-2])# print sec last
print(str1[-3])
print(str1[-4])
print(str1[-5])
print(str1[-6])
print(str1[-7])

# slicing
print(str1[-4:])
print(str1[-6:-2])
print(str1[-6:-2:-1])# wont work prints empty
print(str1[-2:-6:-1])#mocl
print(str1[::-1])# reverse string


#
# for loop

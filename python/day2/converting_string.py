str1="Welcome to Python"

print(str1.capitalize())
var1= str1.title()
print(var1)

print(str1)

print(str1.upper())
print(str1.lower())
print(str1.swapcase())


print(str1.replace("Python", "Java"))
print(str1.replace("o", "i"))


str2="00010203000"
print(str2.strip("0"))
print(str2.lstrip("0"))
print(str2.rstrip("0"))

# string to list
print(str1.split(" "))# list

str3="Welcome, to, Python"
print(str3.split(","))
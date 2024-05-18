str1="Welcome to Python"

# ends -with

print(str1.endswith("on", 1, 17))
print(str1.endswith("to",0,10))

# starts -with

print(str1.startswith("Welcome", 1, 17))
print(str1.startswith("Welcome",0,10))

# finds

print(str1.find("to"))# 8
print(str1.find("to1234"))# -1

# index

print(str1.index("to"))# 8
# print(str1.index("to1234"))# ValueError: substring not found

# count

print(str1.count("o", 4))#3
print(str1.count("123", 1,17))#0
str1="python"
print(str1[0])
# str1[0]="s"#TypeError: 'str' object does not support item assignment

print(id(str1))#1922815314480
print(id(str1+"12345"))#1887627999984
print(id(str1))

str2=str1+"123"
print(id(str1))
print(id(str2))


print(id(str1))
str1=str1+"456"
print(id(str1))

# ordered and immutable

# create tuple

# mytuple=(10, 10.5, "string", [1,2,3,4,5], (1,2,3,4,5))
#
# print(mytuple)
#
# list1=list(mytuple)
# tuple1=tuple(list1)
# tuple12=tuple((1,2,3,4,5))

# empty tuple
# tuple1=()
# tuple2=tuple()
# print(type(tuple2))

# accessing tuple
# tuple1=("apple", "orange", "grape", "kiwi")
#
# print(tuple1[0])
# print(tuple1[1])
# print(tuple1[2])
# print(tuple1[3])
# print(tuple1[-1])
# print(tuple1[::-1])

# for loop
# for i in tuple1:
#     print(i)
#
# for i in tuple1[1:3]:
#     print(i)


# changing/ modfy/remove is not applicable in tuple
# tuple1=("apple", "orange", "grape", "kiwi")
# tuple1[0]="1234"#TypeError: 'tuple' object does not support item assignment
# print(tuple1)


# indirect way
# convert to list
# do the modification
# convert back to tuple

# tuple1=("apple", "orange", "grape", "kiwi")
# print(f"tuple1{tuple1}")
# list1=list(tuple1)
# list1.remove("kiwi")
# print(f"listt1{list1}")
#
# tuple1=tuple(list1)
#
# print(f"tuple1{tuple1}")

####exsisteance of elem


# tuple1=("apple", "orange", "grape", "kiwi")
# print("kiwi" in tuple1)
# print("kiwi" not in tuple1)
#
# ####length
#
# print(len(tuple1))

#####del
# tuple1=("apple", "orange", "grape", "kiwi")
# # del tuple1[0]#TypeError: 'tuple' object doesn't support item deletion
# del tuple1
# print(tuple1)#NameError: name 'tuple1' is not defined.

###################tuple_func
# tuple1=("apple", "orange", "grape", "kiwi", "grape", "grape")
#
# print(tuple1.count("grape"))
# print(tuple1.count("apple"))# num of occ of the elem
#
# print(tuple1.index("grape"))#2
# print(tuple1.index("grape",3))#4

########################combine
# tuple1=("apple", "orange", "grape", "kiwi", "grape", "grape")
# tuple2=(1,2,3,4,5)
#
# tuple3 = tuple1+tuple2
#
# print(tuple3)

#############################comparator
# tuple1=("apple", "orange", "grape", "kiwi", "grape", "grape")
# tuple2=(1,2,3,4,5)
#
# print(tuple1==tuple2)
# print(tuple1!=tuple2)

###########################copy

tuple1=(1,2,3,4,5)
tuple2=tuple1# swallow
print(f"id {id(tuple1)} tuple1 {tuple1}")
print(f"id {id(tuple2)} tuple2 {tuple2}")


tuple3=tuple(tuple1)## swallow
print(f"id {id(tuple1)} tuple1 {tuple1}")
print(f"id {id(tuple3)} tuple3 {tuple3}")

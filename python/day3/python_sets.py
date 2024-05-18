# unordered and mutable

# myset1={1,2,3,"apple", "kiwi"}
# myset1=set({1,2,3,"apple", "kiwi"})
# print(type(myset1))

# empty sets
# myset1={}#---dict
# myset1=set()
# print(type(myset1))

#converting lits/tuple to set
# removing duplicate
# list1=[1,2,2,2,2,2,3,4,5,5,6,7,8]
# appr 1
# set1=set(list1)
# list1=list(set1)
# print(list1)

# without inbuild
#
# list_t=[]
# for i in list1:
#     if i not in list_t:
#         list_t.append(i)
# print(list_t)

# accessing elem
# set1={"apple", "orange", "grape", "kiwi"}
# print(set1)
# print(set1[0])#TypeError: 'set' object is not subscriptable

# for i in set1:
#     if i == "kiwi":
#         print(i)

# add
# set1={"apple", "orange", "grape", "kiwi"}
#
# set1.add("banana")
# print(set1)
#
# set1.update([1,2,3,4,5])
# set1.update((6,7,8))
# set1.update({11,22,33})
#
# print(set1)


# length
# print(len(set1))


# remove
# set1={"apple", "orange", "grape", "kiwi"}
# set1.pop()# random
# set1.remove("orange")
# set1.discard("orange")
# print(set1)

# with non -exsist elem
# set1.remove("orange12345")#KeyError: 'orange12345'
# set1.discard("orange12345")# no error
# print(set1)

# set1.clear()
# print(set1)

#########combine set

# set1={1,2,3,4,10,20}
# set2={10,20,30,1,2,3}
# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1.symmetric_difference(set2))
# # print(set1.symmetric_difference_update(set2))
# # print(set1)
# print(set1.difference(set2))
# # print(set1.difference_update(set2))
# # print(set1)
# print(set2.difference(set1))

#######################################copy

# set1={1,2,3,4,10,20}
# set2=set1# shallow copy
# print(f"id {id(set1)} set1 {set1}")
# print(f"id {id(set2)} set2 {set2}")
#
# set1.add(30)
#
# print(f"id {id(set1)} set1 {set1}")
# print(f"id {id(set2)} set2 {set2}")

# set2=set(set1)# deep copy
# print(f"id {id(set1)} set1 {set1}")
# print(f"id {id(set2)} set2 {set2}")
# set1.add(30)
# print(f"id {id(set1)} set1 {set1}")
# print(f"id {id(set2)} set2 {set2}")

# set2=set1.copy()# deep copy
# print(f"id {id(set1)} set1 {set1}")
# print(f"id {id(set2)} set2 {set2}")
# set2.add(30)
# print(f"id {id(set1)} set1 {set1}")
# print(f"id {id(set2)} set2 {set2}")


#######################frozen set
# unorderd and immutable

set1=frozenset({1,2,3,4,10,20})
print(type(set1))#<class 'frozenset'>

# set1.
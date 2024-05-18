# add
# mylist = ["apple","orange","grape","kiwi"]
# # approach1
# mylist.append("tomato")
# print(mylist)
#
# # apprach2
# mylist.insert(2, "banana")
# print(mylist)

# remove

# appr1
# mylist = ["apple","orange","grape","kiwi",1,2,3,4]
# print(mylist.pop())# rem klast item
# print(mylist)
# print(mylist.pop(1))
# print(mylist)
# print(mylist.pop(3))
# print(mylist)

#appr2
# mylist = ["apple", "orange", "grape", "kiwi", "grape", "grape"]
# mylist.remove("grape")
# print(mylist)
# mylist.remove("grape")
# print(mylist)
# mylist = [1,2,3,4,"apple", "orange", "grape", "kiwi"]
# mylist.remove(3)
# print(mylist)

# appr3
# mylist = ["apple", "orange", "grape", "kiwi", "grape", "grape"]
# print(mylist)
# del mylist[0]
# print(mylist)
#
# # del mylist
# # print(mylist)#NameError: name 'mylist' is not defined. Did you mean: 'list'?

# mylist = ["apple", "orange", "grape", "kiwi", "grape", "grape"]
# mylist.clear()
# print(mylist)

#############combine two list

list1=[1,2,3,4,5]
list2=["apple", "orange", "grape", "kiwi"]

# # app1
# print(list1+list2)

# app2
# list1.extend(list2)
# print(list1)

# list2.extend(list1)
# print(list2)

# app3

# for i in list1:
#     list2.append(i)
#
# print(list2)

# for i in list2:
#     list1.append(i)
#
# print(list1)

# comparator

# print(list1==list2)
# print(list1!=list2)
# list1=[1,2,3,4,5]
# list2=list1# shallow copy
# print(f"id {id(list1)} of {list1}")
# print(f"id {id(list2)} of {list2}")
# list1.remove(5)
# print(f"id {id(list1)} of {list1}")
# print(f"id {id(list2)} of {list2}")

# appr 1 - deep copy
# list1=[1,2,3,4,5]
# list3=list(list1)# deep copy
# print(f"id {id(list1)} of {list1}")
# print(f"id {id(list3)} of {list3}")
# list1.remove(5)
# print(f"id {id(list1)} of {list1}")
# print(f"id {id(list3)} of {list3}")

#app 2 - deep copy
# list1=[1,2,3,4,5]
# list4=list1.copy()# deep copy
# print(f"id {id(list1)} of list1 {list1}")
# print(f"id {id(list4)} of list4{list4}")
# list1.remove(5)
# print(f"id {id(list1)} of list1 {list1}")
# print(f"id {id(list4)} of list4{list4}")
# list4.append(6)
# print(f"id {id(list1)} of list1 {list1}")
# print(f"id {id(list4)} of list4{list4}")


# converting list to string
list1=["welcome", "to", "python"]

print(", ".join(list1))
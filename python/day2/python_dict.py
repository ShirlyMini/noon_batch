# hasp map
# unordered collect of key and value

# prd1 rate1
# prd2 rate1
# pr...

# create dict
# keys are unique but value can be duplicate
# dict1={"brand":"tata", "model":"1234", "year":2024, "seats":5}

# empty
# dict1={}
# dict1=dict()

# with duplicatre key

# dict1={"brand":"tata", "model":"1234", "year":2024, "seats":5, "brand":"tata1","brand":"tata2"}
# print(dict1)

# accessing key
# dict1={"brand":"tata", "model":"1234", "year":2024, "seats":5}
# # appr 1
# print(dict1['brand'])
# print(dict1['model'])
# print(dict1['year'])
#
# # app2
#
# print(dict1.get('brand'))

###################change value(# add and update)
# dict1={"brand":"tata", "model":"1234", "year":2024, "seats":5}
# # single val;ue
# # dict1['brand']="hero"
# dict1["color"]="black"
# print(dict1)

# multiple value
# add and update
# dict1.update({"brand":"hero", "price":1200000})
# print(dict1)


###########################using for loop
# dict1={'brand': 'tata', 'model': '1234', 'year': 2024, 'seats': 5, 'color': 'black'}

# # fetching key
# # appr1
# for i in dict1:
#     print(i)
#
# #appr2
# for i in dict1.keys():
#     print(i)
#
# # fetching values
# for i in dict1.values():
#     print(i)

# for i in dict1.items():
#     print(i)
#     print(i[0])
#     print(i[1])

# for k,v in dict1.items():
#     print(k)
#     print(v)

# ##############check exsistence
# dict1={"brand":"tata", "model":"1234", "year":2024, "seats":5}
# print("year" in dict1.keys())
# print("tata" in dict1.values())
# ############len
# print(len(dict1))

#######################remove

# dict1={"brand":"tata", "model":"1234", "year":2024, "seats":5}
# print(dict1.pop("seats"))
# print(dict1)

# print(dict1.popitem())
# print(dict1)

# del
# del dict1['brand']
# print(dict1)
# del dict1
# print(dict1)#NameError: name 'dict1' is not defined. Did you mean: 'dict'?

# dict1.clear()
#
# print(dict1)

##########################combine

# dict1={"brand":"tata", "model":"1234", "year":2024, "seats":5}
# dict2={"brand1":"hero", "model1":"0001", "year1":2023, "seats1":4}

# print(dict1+dict2)#TypeError: unsupported operand type(s) for +: 'dict' and 'int'

# dict1.update(dict2)
# print(dict1)

#########################copy
# dict1={"brand":"tata", "model":"1234", "year":2024, "seats":5}
# dict2=dict1# swallow
# print(f"id {id(dict1)} dict1 {dict1}")
# print(f"id {id(dict2)} dict2 {dict2}")
# dict1['color']='black'
# print(f"id {id(dict1)} dict1 {dict1}")
# print(f"id {id(dict2)} dict2 {dict2}")

# dict2=dict(dict1)# deep
# dict2=dict1.copy()
# print(f"id {id(dict1)} dict1 {dict1}")
# print(f"id {id(dict2)} dict2 {dict2}")
# dict1['color']='black'
# print(f"id {id(dict1)} dict1 {dict1}")
# print(f"id {id(dict2)} dict2 {dict2}")

#####################################3

str1="string"
list1=[1,2,3,4]
tuple1=(11,22,33)
set1={44,55,66}
dict1={"brand":"tata", "model":"1234", "year":2024, "seats":5}
print(str1*100)
print(list1*4)
print(tuple1*4)
# print(set1*4)#TypeError: unsupported operand type(s) for *: 'set' and 'int'
# print(dict1*4)#TypeError: unsupported operand type(s) for *: 'dict' and 'int'

print(set1+set1)#TypeError: unsupported operand type(s) for +: 'set' and 'set'


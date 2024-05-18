import json

with open(r"C:\Users\user\PycharmProjects\pythonProject_WE_NOON_BATCH\Selenium\day16\testdata_json.json") as json_read:
    json_content = json_read.read()

# print(json_content)

# conv to dic
dict_json = json.loads(json_content)
# print(dict_json['login_data'])

for i in dict_json['login_data'].values():
    print(i)
import yaml

with open(r"C:\Users\user\PycharmProjects\pythonProject_WE_NOON_BATCH\Selenium\day16\test_data_yaml.yml") as yml_read:
    yml_content = yml_read.read()

dict_yml = yaml.load(yml_content, Loader=yaml.FullLoader)
print(dict_yml)
print(dict_yml['login_data'])
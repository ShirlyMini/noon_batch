import xmltodict

with open(r"C:\Users\user\PycharmProjects\pythonProject_WE_NOON_BATCH\Selenium\day16\xml_data.xml") as xml_read:
    xml_content = xml_read.read()

dict_xml = xmltodict.parse(xml_content)
for i in dict_xml['login_data'].values():
    print(i)


import configparser

config_reader = configparser.RawConfigParser()
config_reader.read(r"C:\Users\user\PycharmProjects\pythonProject_WE_NOON_BATCH\hybrid_framework\Configurations\config_data.ini")

class Read_config:
    @staticmethod
    def GetURL():
        return config_reader.get("common data", "url")

    @staticmethod
    def GetUser():
        return config_reader.get("common data", "user")

    @staticmethod
    def GetPassword():
        return config_reader.get("common data", "password")
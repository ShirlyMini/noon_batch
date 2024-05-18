import logging

# print(logging.getLogger())#<RootLogger root (WARNING)>
###### set level

# l = logging.getLogger()
# l.setLevel(logging.DEBUG)
# print(logging.getLogger())

##### get log msg in log file

# logging.basicConfig(filename=r"./test.txt",
#                     filemode="a",
#                     level=logging.INFO,
#                     format="%(asctime)s::%(levelname)s-->%(message)s"
#                     )

#### get log in file as well as console
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s::%(levelname)s-->%(message)s",
                    handlers=[logging.StreamHandler(), logging.FileHandler(filename=r"./test.txt",mode="a",)]
                    )

logging.debug("this is debiug msg")
logging.info("this is info msg")
logging.warning("this is warn msg")
logging.error("this is error msg")
logging.critical("this is critical msg")
import datetime
import logging

def custom_logger():
    ###append
    # file_path=r"C:\Users\user\PycharmProjects\pythonProject_WE_NOON_BATCH\hybrid_framework\Logs\test_log.txt"
    # logging.basicConfig(level=logging.INFO,
    #                     force=True,
    #                     format="%(asctime)s::%(levelname)s::%(message)s",
    #                     handlers=[logging.StreamHandler(),
    #                               logging.FileHandler(filename=file_path, mode="a")]
    #                     )
    ###write
    dt = datetime.datetime.now()

    file_path = fr"C:\Users\user\PycharmProjects\pythonProject_WE_NOON_BATCH\hybrid_framework\Logs\test_log_{dt.strftime('%d-%m-%Y-%H-%M-%S')}.txt"
    logging.basicConfig(level=logging.INFO,
                        force=True,
                        format="%(asctime)s::%(levelname)s::%(message)s",
                        handlers=[logging.StreamHandler(),
                                  logging.FileHandler(filename=file_path, mode="w")]
                        )
    return logging
import logging
# 打印格式
LOG_FORMAT = "%(asctime)s======%(levelname)s+++++++%(message)s"
# 日志配置
# 只写文件名不写路径,默认保存在当前目录
logging.basicConfig(filename="logfile.log", level=logging.DEBUG, format=LOG_FORMAT)
# 一种写法
logging.warning("this is a warning log")
# 另一种写法
logging.log(logging.WARNING, "this is a warning log")

logging.log(logging.DEBUG, "this is a debug log")

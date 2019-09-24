"""
利用Logging函数模块可以进行日志的输出，使用函数的过程如下，需要设置log_format="%(asctime)s - %(levelname)s - %(message)s"
即输出的形式以及时间显示的形式datefmt = "%I:%M:%S %P %d/%m/%y'
"""
# 利用logging函数进行日志输出
# import logging
# LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
# DATE_FORMAT = '%I:%M:%S %P %d/%m/%y'
# logging.basicConfig(level=logging.INFO, format=LOG_FORMAT, datefmt=DATE_FORMAT)
# logging.debug('This is a debug log')
# logging.info('This is a info log')
# logging.warning('This is a warning log')
# logging.error('This is a error log')
# logging.critical('This is a critial log')

####利用loggin的四大组件进行日志输出
import logging
import logging.handlers
import datetime

logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

f_hander = logging.FileHandler("error.log")
f_hander.setLevel(logging.ERROR)
f_hander.setFormatter(logging.Formatter("%(asctime)s-%(levelname)s-%(filename)s[:%(lineno)d-%(message)s]"))
logger.addHandler(f_hander)

logger.debug('This is a debug log')   ##其实message就是一个字符串，最后传入一个字符串就好
logger.info('This is a info log')
logger.warning('This is a warning log')
logger.error('This is a error log')
logger.critical('This is a critial log')


import logging
from logging import Formatter, FileHandler

logger = logging.getLogger('demo')
logger.setLevel(logging.INFO)

handler = FileHandler('E:/code/python/examples/demo/xx.log')
handler.setLevel(logging.INFO)
fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'
formatter = logging.Formatter(fmt) # 实例化formatter
handler.setFormatter(formatter) # 为handler添加formatter
logger.addFilter(handler)

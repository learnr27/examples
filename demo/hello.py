import random
from demo.log_ import logger

logger.info('sas的士速递')
a = ['石头', '剪刀', '步']

random.shuffle(a)
print(random.sample(a,2))





# 说明
# dir(__builtins__) python 内置函数
# eval 输入类型必须数字类
# help('keywords')  保留字
# help('modules') 获取标准库
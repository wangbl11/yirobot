import random
import math
# 初始化m个数组, 数组中数字的范围在0-n，数组的大小是随机的
arrays=[]
def init(m,n):
    one=[]
    _lens = random.sample(range(1, n), m)
    for i in range(m):
        arrays.append(random.sample(range(1,n),_lens[i]))
    return arrays
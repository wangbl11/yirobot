import random
import math
# 初始化m个数组, 数组中数字的范围在0-n，数组的大小是随机的
arrays=[]
def init(m,n):
    one=[]
    _lens = random.sample(range(1, n), m)
    for i in range(m):
        arrays.append(random.sample(range(1,n),_lens[i]))

# 冒泡
def bubble(idx):
    _len=len(arrays[idx])
    _array=arrays[idx]
    print(_array)
    for i in range (1,_len):
        for j in range(1,_len+1-i):
            if _array[j-1]>_array[j]:
                _t=_array[j-1]
                _array[j-1]=_array[j]
                _array[j]=_t
    print(_array)

# 梳，在冒泡排序前做一些排序
def comb(idx):
    _len=len(arrays[idx])
    _array=arrays[idx]
    print(_array)

    # 步长
    j=_len
    s=1.3
    flag=False
    while j>1:
        #内层，
        i=0
        j=max(math.floor(j/s),1)
        flag=False
        # 比较
        while i+j<_len:
            if _array[i]>_array[i+j]:
                _t=_array[i]
                _array[i]=_array[i+j]
                _array[i+j]=_t
                flag=True
            i+=1
    print(_array)

# 堆
def heap(idx):
    _len=len(arrays[idx])
    _array=arrays[idx]
    print(_array)
    #自己实现二叉树


def mergesort(idx):
    pass

def quicksort(idx):
    pass

def timsort(idx):
    pass

init(3,10)
bubble(0)
comb(1)
heap(2)
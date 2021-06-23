"""
假如有 100 个小文件，每个小文件都为 100 MB，每个小文件中存储的都是有序的字符串，现在要求合并成一个有序的大文件，
"""
import heapq
import os
files=[]
for i in range(1,6):
    with open('../data/00'+str(i)+'.txt',mode='rt') as f:
        lines=f.read().splitlines()
        lines=[one for one in lines if len(one)>0]
        # print(lines)
        # files.append(lines)
        # heapq.heapify(lines)
        files.append(lines)

# # 使用merge的方法
# _final=[]
# iter=heapq.merge(*files)
# for one in iter:
#     _final.append(one)
# ## 去重操作
# _final=set(_final)
# print(_final)

# 使用pop的原始方法
## 初始化
_pool=[]
for i in range(0,5):
    heapq.heappush(_pool,(heapq.heappop(files[i]),i))
## 不断取出
while len(_pool)>0:
    one = heapq.heappop(_pool)
    print(one)
    _src=one[1]

    if len(files[_src])>0:
      heapq.heappush(_pool,(heapq.heappop(files[_src]),_src))


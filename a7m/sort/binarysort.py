"""
  二分插入排序，也叫插入排序法。在数据量比较小的情况下效率较高。
  最差情况下它需要 O(n log n) 次比较和 O(n^2)次数据移动。
"""

import math
from a7m.sort.seeds import init


def binary_insert_sort(l):
    length = len(l)
    for i in range(1, length):
        be, en = 0, i - 1
        mid = (en + be) // 2

        while True:
            if mid < 0 or l[mid] == l[i] or (be >= en):
                if mid >= 0 and l[mid] > l[i]:
                    l.insert(mid, l.pop(i))
                else:
                    l.insert(mid + 1, l.pop(i))
                break
            elif l[mid] > l[i]:
                en = mid - 1
            else:
                be = mid + 1
            mid = (en + be) // 2

    return l

def binarysort(a):
    a_len=len(a)
    for i in range(1,a_len):
        binarySort(a,0,i,i)

"""
lo：待排序范围内的首个元素的位置
hi：待排序范围内最后一个元素的后一个位置
start：待排序范围内的第一个没有排好序的位置，确保 (lo <= start <= hi)
"""
def binarySort(a,lo,hi,start):
    if lo>start or start>hi:
        raise Exception("range错误")

    if start ==lo:
        start+=1

    for i in range(start,hi if start<hi else hi+1):
        pivot=a[start]

        # 把pivot应当插入的位置的起始边界设置为left和right
        left=lo
        right=start

        while left<right:
            mid=math.floor((left+right)/2)
            if pivot<a[mid]:
                right=mid
            else:
                left=mid+1

        # 此时，仍然能保证：
        # pivot > [lo,left) && pivot < [left,start)
        # 索引，pivot的值应当在left所在的位置，然后需要把[left, start)范围内的内容整体右移一位
        # 腾出空间。如果pivot与区间中的某个值想疼，left会只想重复的值的后一位。
        # 所以这里的排序是稳定的。
        for i in range(start, left,-1):
            a[i]=a[i-1]
        a[left]=pivot

_todo=init(1,100)[0]
print(_todo)
binarysort(_todo)
print(_todo)
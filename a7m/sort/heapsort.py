"""
堆排序
python中有一个已经实现好的堆heapq，此处我们要用基本数据结构实现
"""
from a7m.sort.seeds import init

"""
最小堆
"""
def heapifys(arr,n,i):
    # print(n,i,sep=" ")
    smallest=i
    l=2*i+1
    r=2*i+2
    if l<n and arr[smallest]>arr[l]:
        smallest=l
    if r<n and arr[smallest]>arr[r]:
        smallest=r
    if smallest!=i:
        arr[i],arr[smallest]=arr[smallest],arr[i]
        heapifys(arr,n,smallest)



"""
最大堆
"""
def heapifyb(arr,n,i):
    # print(n,i,sep=" ")
    larget=i
    l=2*i+1
    r=2*i+2
    if l<n and arr[larget]<arr[l]:
        larget=l
    if r<n and arr[larget]<arr[r]:
        larget=r
    if larget!=i:
        arr[i],arr[larget]=arr[larget],arr[i]
        heapifyb(arr,n,larget)


"""
前m个最小的数
"""
def heapsorts(arr,m):
    if not arr:
        return
    n=len(arr)
    if n<=m:
        return arr

    # 构建堆
    n = len(arr)
    for i in range(n, -1, -1):
        heapifys(arr, n, i)

    # 出堆，初始时
    # 一次决选出一个最大的，放入到数组尾部（相当与出堆)
    steps=0 if n-m-2<0 else n-m-2
    for i in range(n-1,steps,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapifys(arr,i,0)

    return arr[n-m:]

"""
从小到小完全排序
"""
def heapsortsb(arr):
    # 构建堆
    n=len(arr)
    for i in range(n,-1,-1):
        heapifyb(arr,n,i)

    # 出堆，初始时
    # 一次决选出一个最大的，放入到数组尾部（相当与出堆)
    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapifyb(arr,i,0)



"""
从大到小完全排序
"""
def heapsortbs(arr):
    # 构建堆
    n=len(arr)
    for i in range(n,-1,-1):
        heapifys(arr,n,i)

    # 出堆，初始时
    # 一次决选出一个最大的，放入到数组尾部（相当与出堆)
    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapifys(arr,i,0)

arr=init(1,30)[0]
print(arr)

# heapsortsb(arr)
# print(arr)
# heapsortbs(arr)
# print(arr)

#最小的m个
rst=heapsorts(arr,len(arr)-3)
print(rst)
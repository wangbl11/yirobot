"""
https://www.jianshu.com/p/892ebd063ad9
https://svn.python.org/projects/python/trunk/Objects/listsort.txt
https://hg.python.org/cpython/file/5c1bacba828d/Objects/listobject.c
https://www.infopulse.com/blog/timsort-sorting-algorithm/
https://github.com/RonTang/SimpleTimsort/blob/master/SimpleTimsort.py
是归并排序法和插入排序法的结合

"""

class timsort:
    def __init__(self,a):
        self.a=a;
        a_len=len(a)
        self.minRun=32
        self.minRun=self.dyminRun(a_len)

    def dyMinRun(self,n):
        # becomes 1 if the least significant bits contain at least one off bit
        r=0
        while n>=64:
            r|=n&1
            n>>=1
        return n+r

    def rangeCheck(self,len,fromIdx,toIdx):
        if fromIdx>toIdx:
            raise Exception("fromdx>toIdx")
        if fromIdx<0:
            raise Exception("fromIdx<0")
        if toIdx>len:
            raise Exception("toIdx>len")

    def sort(self):
        self.sort(self.a,0,len(self.a))


    def sort(self,array,lo,hi):
        self.rangeCheck(len(array),lo,hi)

        nRemaining=hi-lo

        if nRemaining<2:
            return

        # 小于MIN_MERGE长度的数组就不用归并排序了
        if nRemaining<self.minRun:
            pass



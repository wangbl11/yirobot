# https://www.jianshu.com/p/e0a40d6748b8

import heapq
import random
import math
stream = []


def init(n=10):
    for i in range(n):
        stream.append(random.uniform(1, 100))
    # print(stream)


class median:
    def __init__(self, percent):
        self._big = []
        self._little = []
        self.percent = percent / 100

        self._percent = round(1 - self.percent,1)
        print(self.percent,self._percent)
        self.sum = 0

    def insert(self, data):
        if len(self._big) == 0 or data > -self._big[0]:
            heapq.heappush(self._big, -data)
        else:
            heapq.heappush(self._little, data)
        self.sum += 1
        # 调整数组大小
        _expected_big=math.ceil(self.sum*self.percent)-1
        _expected_little=self.sum-_expected_big

        while self.sum > 1 and len(self._big)>_expected_big:
            heapq.heappush(self._little, heapq.heappop(self._big)*-1)
        while self.sum > 1 and len(self._little) >  _expected_little:
            heapq.heappush(self._big, heapq.heappop(self._little) * -1)

    def get(self):
        print(self._big)
        print(self._little)
        if len(self._big)>0:
            return -self._big[0]
        return 0
    def loopb(self):
        while len(self._big)>0:
            print(heapq.heappop(self._big))

init(9)
_me=median(50)
for one in stream:
   _me.insert(one)
print(_me.get())
_me.loopb()

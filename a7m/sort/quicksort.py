"""
快速排序，递归方法
"""
from a7m.sort.seeds import init
import math

def quicksort(_todo):

  _len=len(_todo)
  _first=_todo[0]
  _last=_todo[-1]
  _mid=_todo[math.floor(_len/2)]
  _median=(_first+_last+_mid)/3
  _little=[]
  _big=[]
  _eq=[]
  for one in _todo:
      if one<_median:
          _little.append(one)
      elif one>_median:
          _big.append(one)
      else:
          _eq.append(one)
  if len(_big)>0:
      _big=quicksort(_big)
  if len(_little)>0:
      _little=quicksort(_little)
  return _little+_eq+_big



_todo=init(1,100)[0]
_done=quicksort(_todo)
print(_done)


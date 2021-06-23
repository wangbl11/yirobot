"""
djb2
"""
from functools import reduce


def djb2(val):
    h=0
    for one in val:
       h=(h<<6)+h+ord(one)
       print(h)

from ctypes import c_ulong

def ulong(i): return c_ulong(i).value  # numpy would be better if available

def djb2(L):
  """
  h = 5381
  for c in L:
    h = ((h << 5) + h) + ord(c) # h * 33 + c
  return h
  """
  return reduce(lambda h,c: ord(c) + ((h << 5) + h), L, 5381)

def djb2_l(L):
  return reduce(lambda h,c: ulong(ord(c) + ((h << 5) + h)), L, 5381)

def sdbm(L):
  """
  h = 0
  for c in L:
    h = ord(c) + (h << 6) + (h << 16) - h
  return h
  """
  return reduce(lambda h,c: ord(c) + (h << 6) + (h << 16) - h, L, 0)

def sdbm_l(L):
  return reduce(lambda h,c: ulong(ord(c) + (h << 6) + (h << 16) - h), L, 0)

def loselose(L):
  """
  h = 0
  for c in L:
    h += ord(c);
    return h
  """
  return sum(ord(c) for c in L)
djb2("ab")
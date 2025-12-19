#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#03_demo : 3121910778619
#03_01 : 171518260283767

import sys

if len(sys.argv) != 2:
  print(f"Usage: {sys.argv[0]} <input file>")
  sys.exit(1)

def del_min(val):
  m, a = int(val[0]), 0
  for i in range(1, len(val)):
    if int(val[i]) > m: break
    else: m, a = int(val[i]), i
  return val[0:a] + val[a+1:]

filename = sys.argv[1]
try:
  with open(filename, 'r', encoding='utf-8') as f:
    output = 0
    for v in f.readlines():
      v = v.strip()
      while len(v) > 12: v = del_min(v)
      output += int(v)
    print(output)
except FileNotFoundError:
  print(f"File not found: {filename}")
  sys.exit(1)

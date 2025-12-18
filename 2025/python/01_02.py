#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#01_demo : 6
#01_01 : 6289

import sys

if len(sys.argv) != 2:
  print(f"Usage: {sys.argv[0]} <input file>")
  sys.exit(1)

filename = sys.argv[1]
try:
  with open(filename, 'r', encoding='utf-8') as f:
    index = 50
    password = 0
    for v in f.readlines():
      vv = int(v.strip().replace('L', '-').replace('R', '+'))
      index_new = index + vv
      if index_new < 0 or index_new >= 100: password += abs(index_new // 100)
      if index_new // 100 < 0 and index == 0: password -= 1
      index = index_new % 100
      if index + vv < 0 and index == 0: password += 1
    print(password)
except FileNotFoundError:
  print(f"File not found: {filename}")
  sys.exit(1)

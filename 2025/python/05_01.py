#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#05_demo : 3
#05_01 : 643

import sys

if len(sys.argv) != 2:
  print(f"Usage: {sys.argv[0]} <input file>")
  sys.exit(1)

filename = sys.argv[1]
try:
  with open(filename, 'r', encoding='utf-8') as f:
    output = 0
    do_range = True
    ranges = []
    for v in f.readlines():
      v = v.strip()
      if v == '':
        do_range = False
        continue
      if do_range == True:
        tmp = v.split('-')
        for i in range(len(tmp)): tmp[i] = int(tmp[i])
        ranges.append(tmp)
      else:
        for r in ranges:
          if r[0] <= int(v) <= r[1]:
            output += 1
            break
    print(output)
except FileNotFoundError:
  print(f"File not found: {filename}")
  sys.exit(1)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#02_demo : 4174379265
#02_01 : 22617871034

import sys

if len(sys.argv) != 2:
  print(f"Usage: {sys.argv[0]} <input file>")
  sys.exit(1)

filename = sys.argv[1]
try:
  with open(filename, 'r', encoding='utf-8') as f:
    output = 0
    for v in f.readlines():
      for r in v.strip().split(','):
        r = r.split('-')
        for i in range(int(r[0]), int(r[1])+1):
          ii = str(i)
          iii = len(ii)
          for l in range(1, int(iii / 2) + 1):
            if iii % l != 0: break
            chunk = [ ii[t:t+l] for t in range(0, iii, l) ]
            equal = True
            for t in chunk:
              if t != chunk[0]:
                equal = False
                break
            if equal == True:
              output += i
              break
    print(output)
except FileNotFoundError:
  print(f"File not found: {filename}")
  sys.exit(1)

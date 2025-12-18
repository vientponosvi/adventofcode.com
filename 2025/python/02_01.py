#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#02_demo : 1227775554
#02_01 : 15873079081

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
          if iii % 2 == 0 and ii[0:int(iii/2)] == ii[int(iii/2):]: #Seulement les nombres d'une taille pair
            output += i
    print(output)
except FileNotFoundError:
  print(f"File not found: {filename}")
  sys.exit(1)

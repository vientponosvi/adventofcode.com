#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#03_demo : 357
#03_01 : 17330

import sys

if len(sys.argv) != 2:
  print(f"Usage: {sys.argv[0]} <input file>")
  sys.exit(1)

filename = sys.argv[1]
try:
  with open(filename, 'r', encoding='utf-8') as f:
    output = 0
    for v in f.readlines():
      v = v.strip()
      dizaine, unite = int(v[0]), int(v[-1])
      for i in range(1, len(v)-1):
        if int(v[i]) > dizaine:
          dizaine, unite = int(v[i]), int(v[-1])
        elif int(v[i]) > unite:
          unite = int(v[i])
      output += dizaine * 10 + unite
    print(output)
except FileNotFoundError:
  print(f"File not found: {filename}")
  sys.exit(1)

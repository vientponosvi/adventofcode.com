#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
      index = (index + int(v.strip().replace('L', '-').replace('R', '+'))) % 100
      if index == 0: password += 1
    print(password)
except FileNotFoundError:
  print(f"File not found: {filename}")
  sys.exit(1)

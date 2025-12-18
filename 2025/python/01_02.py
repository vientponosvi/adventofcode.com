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
      p = -1 if v.startswith('L') else 1
      for _ in range(int(v.strip()[1:])):
        index += p
        if index < 0: index = 99
        elif index > 99: index = 0
        if index == 0: password += 1
    print(password)
except FileNotFoundError:
  print(f"File not found: {filename}")
  sys.exit(1)

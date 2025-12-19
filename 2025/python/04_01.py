#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#04_demo : 13
#04_01 : 1441

import sys

if len(sys.argv) != 2:
  print(f"Usage: {sys.argv[0]} <input file>")
  sys.exit(1)

def getChar(val, index):
  if index == -1: return '.'
  try:
    return val[index]
  except IndexError:
    return '.'

filename = sys.argv[1]
try:
  with open(filename, 'r', encoding='utf-8') as f:
    output = 0
    line_before = ''
    line_current = f.readline().strip()
    line_after = f.readline().strip()
    while True:
      for i, c in enumerate(line_current):
        if c == '.': continue
        nb = -1
        for ii in range(i-1, i+2):
          for l in (line_before, line_current, line_after):
            if getChar(l, ii) == '@': nb += 1
        if nb < 4: output += 1
      line_before = line_current
      line_current = line_after
      line_after = f.readline().strip()
      if line_current == '' and line_after == '': break
    print(output)
except FileNotFoundError:
  print(f"File not found: {filename}")
  sys.exit(1)

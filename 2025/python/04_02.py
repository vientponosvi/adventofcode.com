#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#04_demo : 43
#04_01 : 9050

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
    lines = []
    line_before = ''
    line_current = f.readline().strip()
    line_after = f.readline().strip()
    while True:
      lines.append(list(line_current))
      for i, c in enumerate(line_current):
        if c == '.': continue
        nb = -1
        for ii in range(i-1, i+2):
          for l in (line_before, line_current, line_after):
            if getChar(l, ii) == '@': nb += 1
        if nb < 4:
          output += 1
          lines[len(lines)-1][i] = 'x'
      line_before = line_current
      line_current = line_after
      line_after = f.readline().strip()
      if line_current == '' and line_after == '': break
    while True:
      o = 0
      for i, l in enumerate(lines):
        for ii, c in enumerate(l):
          if c != '@': continue
          nb = 0
          if i > 0:
            if ii > 0 and lines[i-1][ii-1] == '@': nb += 1
            if lines[i-1][ii] == '@': nb += 1
            if ii < len(lines[i-1]) - 1 and lines[i-1][ii+1] == '@': nb += 1
          if ii > 0 and lines[i][ii-1] == '@': nb += 1
          if ii < len(lines[i]) - 1 and lines[i][ii+1] == '@': nb += 1
          if i < len(lines) - 1:
            if ii > 0 and lines[i+1][ii-1] == '@': nb += 1
            if lines[i+1][ii] == '@': nb += 1
            if ii < len(lines[i+1]) - 1 and lines[i+1][ii+1] == '@': nb += 1
          if nb < 4:
            o += 1
            lines[i][ii] = 'x'
      #print(o)
      #for l in lines: print(l)
      if o == 0: break
      output += o
    print(output)
except FileNotFoundError:
  print(f"File not found: {filename}")
  sys.exit(1)

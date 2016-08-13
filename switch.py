#!/usr/bin/env python3
from orvibo.s20 import S20
import sys

try:
  ip = sys.argv[1]
except IndexError:
  print ("IP required. e.g. switch.py 10.1.1.1. ON")
  sys.exit(1)

switch = S20(ip)

if len(sys.argv) > 3:
  action = sys.argv[2]  
  if(action == "ON"):
    state = True
  elif (action == "OFF"):
    state = False
  else:
    raise RuntimeError("Unrecognised state: " + action)

  switch.on = state

else:
  if switch.on:
    print('ON')
  else:
    print('OFF')




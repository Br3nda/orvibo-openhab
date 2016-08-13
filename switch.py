#!/usr/bin/env python3
from orvibo.s20 import S20
import sys

try:
  ip = sys.argv[1]
  action = sys.argv[2]
except IndexError:
  print ("IP and action required. e.g. switch.py 10.1.1.1. ON")
  sys.exit(1)
  

if(action == "ON"):
  state = True
elif (action == "OFF"):
  state = False
else:
  raise RuntimeError("Unrecognised state: " + action)

S20(ip).on = state

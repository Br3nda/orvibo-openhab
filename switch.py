#!/usr/bin/env python3
from orvibo.s20 import S20
import sys

ip = sys.argv[1]
action = sys.argv[2]

if(action == "ON"):
  state = True
elif (action == "OFF"):
  state = False
else:
  raise RuntimeError("Unrecognised state: " + action)

S20(ip).on = state

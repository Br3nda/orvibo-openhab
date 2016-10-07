#!/usr/bin/env python3
from orvibo.s20 import S20
import sys
import time
import fasteners


def change_switch_state(ip, action):
  print("Changing switch state")
  if(action == "ON"):
    state = True
  elif (action == "OFF"):
    state = False
  else:
    raise RuntimeError("Unrecognised state: " + action)
  S20(ip).on = state


@fasteners.interprocess_locked('/tmp/orvibo_lock_file')
def switch():
  if len(sys.argv) >= 3:
    action = sys.argv[2]
    change_switch_state(ip, action)

  if S20(ip).on:
    print('ON')
  else:
    print('OFF')

try:
  ip = sys.argv[1]
except IndexError:
  print ("IP required. e.g. switch.py 10.1.1.1. ON")
  sys.exit(1)

switch()



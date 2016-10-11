#!/usr/bin/env python3
from orvibo.s20 import S20, discover
import fasteners
import argparse


def change_switch_state(ip, action):
  if(action == "ON"):
    state = True
  elif (action == "OFF"):
    state = False
  else:
    raise RuntimeError("Unrecognised state: " + action)
  S20(ip).on = state


@fasteners.interprocess_locked('/tmp/orvibo_lock_file')
def switch(ip, action):
  if action:
    change_switch_state(ip, action)
  elif ip:
    if S20(ip).on:
      print('ON')
    else:
      print('OFF')
  else:
    hosts = discover()
    for host in hosts.keys():
      print (host)


parser = argparse.ArgumentParser(description='Query and command an orvibo switch')
parser.add_argument('ip', nargs='?', help='ip of switch')
parser.add_argument('action', nargs='?', help='action')
args = parser.parse_args()

switch(ip=args.ip, action=args.action)

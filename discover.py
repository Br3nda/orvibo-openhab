#!/usr/bin/python3
from orvibo.s20 import discover
hosts = discover() # Discover devices on your local network.
print(hosts.keys())


#!/usr/bin/python3

import pandas as pd 
from matplotlib import pyplot as plt 

spike_log = open("demo/serial-simtiny-workload.log", "r")

insn_dct = {}
for line in spike_log:
  line_list = line.split();
  if(len(line_list) > 5):
    key = line_list[4]
    insn_dct[key] = insn_dct.get(key, 0) + 1
    # print(insn_dct[key]) 

for kv in insn_dct.items():
  print(kv)

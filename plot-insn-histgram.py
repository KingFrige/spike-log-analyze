#!/usr/bin/python3

import pandas as pd 
from matplotlib import pyplot as plt 

width,height=20,30
plt.rcParams['figure.figsize'] = width, height

spike_log = open("demo/serial-simtiny-workload.log", "r")

insn_dct = {}
for line in spike_log:
  line_list = line.split();
  if(len(line_list) > 5):
    key = line_list[4]
    insn_dct[key] = insn_dct.get(key, 0) + 1

insn_sorted = sorted(insn_dct.items(), key = lambda kv: kv[1], reverse=True)

x1 = [x[0] for x in insn_sorted]
y1 = [x[1] for x in insn_sorted] 

# Figure Size 
fig, ax = plt.subplots(figsize=(16, 32)) 

# Horizontal Bar Plot 
ax.barh(x1, y1) 

# Remove axes splines 
for s in ['top', 'bottom', 'left', 'right']:
  ax.spines[s].set_visible(False) 

# Remove x, y Ticks 
ax.xaxis.set_ticks_position('none') 
ax.yaxis.set_ticks_position('none') 

# Add padding between axes and labels 
ax.xaxis.set_tick_params(pad=5) 
ax.yaxis.set_tick_params(pad=10) 

ax.grid(b=True, color='grey', 
  linestyle='-.', linewidth=0.5, 
  alpha=0.2) 

ax.invert_yaxis() 

for i in ax.patches:
  plt.text(i.get_width()+0.2, i.get_y()+0.5, 
    str(round((i.get_width()), 2)), 
    fontsize=10, fontweight='bold', 
    color='grey') 

ax.set_title('pc histgram', 
  loc='left', ) 

fig.text(0.9, 0.15, 'test', fontsize=12, 
  color='grey', ha='right', va='bottom', 
  alpha=0.7) 

plt.title('insn histogram')
plt.savefig('output/insn-histogram.png', dpi=300)

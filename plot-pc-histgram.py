#!/usr/bin/python3

import pandas as pd 
from matplotlib import pyplot as plt 
import argparse
import os

parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument("--path", type=str, default="0")
args = parser.parse_args()

path_base = os.path.basename(args.path) 
file_name = path_base.split('.')[0]

# Read CSV into pandas 
data = pd.read_csv(args.path, dtype={'pc': str, 'times': int}) 
# print(data.dtypes)

data.head() 
df = pd.DataFrame(data) 
data_dict = dict(df.to_dict('split')['data'])
data_sorted = sorted(data_dict.items(), key = lambda kv: kv[1], reverse=True)
# print(data_sorted)

pc_addrs = [x[0] for x in data_sorted[:40]]
ex_times = [x[1] for x in data_sorted[:40]] 

# Figure Size 
fig, ax = plt.subplots(figsize=(16, 9)) 

# Horizontal Bar Plot 
ax.barh(pc_addrs, ex_times) 

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

plt.savefig('output/'+file_name+'-pc-histogram.png', dpi=300)
plt.show()


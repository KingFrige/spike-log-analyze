#!/usr/bin/python3


import pandas as pd 
from matplotlib import pyplot as plt 

# Read CSV into pandas 
data = pd.read_csv(r"demo/test.csv") 
data.head() 
df = pd.DataFrame(data) 
data_dict = df.to_dict('split')
print("data_dict = ", data_dict['columns'])
# print(sorted(data_dict.items(), key = lambda kv:(kv[1], kv[0]), reverse=True))

pc_addr = df['pc'].head(20)
ex_times = df['times'].head(20)

# Figure Size 
fig, ax = plt.subplots(figsize=(16, 9)) 

# Horizontal Bar Plot 
ax.barh(pc_addr, ex_times) 

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

ax.set_title('tttttt', 
  loc='left', ) 

fig.text(0.9, 0.15, 'test', fontsize=12, 
  color='grey', ha='right', va='bottom', 
  alpha=0.7) 

plt.show()

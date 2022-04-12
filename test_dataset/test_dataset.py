import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import gridspec

cat_c = []
for i in range(23):
    cat_c.append('c'+str(i+1))
cat_c_num = [30, 40, 15, 10, 40, 35, 30, 30, 22, 5, 45, 30, 35, 45, 30, 30, 30, 30, 17, 38, 38, 37, 38]

cat_r = []
for i in range(34):
    cat_r.append('r'+str(i+1))
cat_r_num = [30, 40, 15, 10, 40, 35, 30, 30, 22, 5, 45, 30, 35, 45, 30, 30, 30, 30, 17, 40, 8, 42, 18, 40, 30, 15, 25, 45, 52, 30, 6, 30, 35, 35]

df_c = pd.DataFrame({'C23':cat_c, 'Number':cat_c_num})
df_r = pd.DataFrame({'R34':cat_r, 'Number':cat_r_num})

#df_c['Number'].describe()

SMALL_SIZE = 8
MEDIUM_SIZE = 12
BIGGER_SIZE = 14

plt.rc('font', size=BIGGER_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=BIGGER_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=BIGGER_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=BIGGER_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

plt.figure(figsize=(15,4))
plt.xticks(rotation=90)
sns.barplot(x='C23', y='Number', data=df_c, color='#3F466E')
#ax.bar_label(ax.containers[0])
for i, v in enumerate(df_c['Number']):
    plt.text(i - 0.22 , v + 0.8, v)
plt.xlabel(None)
plt.ylabel(None)
plt.ylim(0, 50)
plt.savefig('c23_bar.png', transparent=True)

plt.figure(figsize=(15,4))
plt.xticks(rotation=90)
sns.barplot(x='R34', y='Number', data=df_r, color='#3F466E')
#ax.bar_label(ax.containers[0])
for i, v in enumerate(df_r['Number']):
    plt.text(i - 0.35 , v + 0.8, v)
plt.xlabel(None)
plt.ylabel(None)
plt.ylim(0, 60)
plt.savefig('r34_bar.png', transparent=True)

plt.figure(figsize=(15,4))
gs = gridspec.GridSpec(1, 2, width_ratios=[3, 1]) 
plt.subplot(gs[0])
plt.xticks(rotation=90)
ax = sns.barplot(x='C23', y='Number', data=df_c, color='#3F466E')
#ax.bar_label(ax.containers[0])
for i, v in enumerate(df_c['Number']):
    plt.text(i - 0.32 , v + 0.5, v)
ax.set(xlabel=None)
ax.set(ylabel=None)
ax.set(ylim=(0, 50))
plt.subplot(gs[1])
ax = sns.distplot(df_c['Number'])
ax.set(xlabel=None)
ax.set(ylabel=None)
plt.savefig('c23_dist.png', transparent=True)


plt.figure(figsize=(15,3))
plt.subplot(1,2,1)
ax = sns.distplot(df_c['Number'])
ax.set(xlabel=None)
plt.subplot(1,2,2)
ax = sns.boxplot(df_c['Number'])
ax.set(xlabel=None)


plt.figure(figsize=(15,4))
gs = gridspec.GridSpec(1, 2, width_ratios=[3, 1]) 
plt.subplot(gs[0])
plt.xticks(rotation=90)
ax = sns.barplot(x='R34', y='Number', data=df_r, color='#3F466E')
#ax.bar_label(ax.containers[0])
for i, v in enumerate(df_r['Number']):
    plt.text(i - 0.44 , v + 0.5, v)
ax.set(xlabel=None)
ax.set(ylabel=None)
ax.set(ylim=(0, 60))
plt.subplot(gs[1])
ax = sns.distplot(df_r['Number'])
ax.set(xlabel=None)
ax.set(ylabel=None)
plt.savefig('r34_dist.png', transparent=True)


plt.figure(figsize=(15,3))
plt.subplot(1,2,1)
ax = sns.distplot(df_r['Number'])
ax.set(xlabel=None)
plt.subplot(1,2,2)
ax = sns.boxplot(df_r['Number'])
ax.set(xlabel=None)

plt.figure(figsize=(15,3))
plt.subplot(1,2,1)
sns.boxplot(df_c['Number'])
plt.subplot(1,2,2)
sns.boxplot(df_r['Number'])

#sns.displot(df_c['Number'], kde=True)
#sns.displot(df_r['Number'], kde=True)

plt.figure(figsize=(10,5))
sns.distplot(df_c['Number'])
sns.distplot(df_r['Number'])
plt.legend(labels=["C23","R34"], title = "Category")
plt.xlabel(None)
plt.ylabel(None)
plt.savefig('c23_r34_dist.png', transparent=True)

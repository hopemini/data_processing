import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

cat_c = []
for i in range(23):
    cat_c.append('c'+str(i+1))
cat_c_num = [30, 40, 15, 10, 40, 35, 30, 30, 22, 5, 45, 30, 35, 45, 30, 30, 30, 30, 17, 38, 38, 37, 38]

cat_r = []
for i in range(34):
    cat_r.append('c'+str(i+1))
cat_r_num = [30, 40, 15, 10, 40, 35, 30, 30, 22, 5, 45, 30, 35, 45, 30, 30, 30, 30, 17, 40, 8, 42, 18, 40, 30, 15, 25, 45, 52, 30, 6, 30, 35, 35]

cat_c_num.describe()

#plt.figure(figsize=(10, 8))
plt.xticks(rotation=90)
plt.bar(cat_c, cat_c_num,)
#sns.barplot(cat_c, cat_c_num,)
plt.show()

sns.violinplot(cat_c_num)
plt.show()

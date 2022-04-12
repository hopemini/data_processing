import argparse
import glob
import os
from tqdm import tqdm
import matplotlib.pyplot as plt

par = argparse.ArgumentParser()
par.add_argument("-t", "--types", default="semantic", choices=["real", "semantic_annotations"],
                 type=str, help="Choose a data type. (real/semantic_annotations)")
par.add_argument("-c", "--number_of_classes", default=34,
                 type=int, help="number of classes")
par.add_argument("-js", "--jsd", action='store_true', help="use js-divergence")
par.add_argument("-d", "--directory", default=".",
                 type=str, help="directory for plotting losses")
args = par.parse_args()

types = args.types
num_classes = args.number_of_classes

log_path = args.directory + "/log/check_point/"
log_path = (log_path + ("re" if types == "real" else "se") + "_" + str(num_classes) + "/")


fig_path = args.directory + "/log/plot/"

if not os.path.isdir(fig_path):
    os.mkdir(fig_path)

if args.jsd:
    epoch_fmt = '_jsd_idec_epoch'
else:
    epoch_fmt = '_idec_epoch'

num = list()
for f in tqdm(glob.glob(log_path + "*")):
    num.append(int(f.split('epoch')[-1]))

num.sort()
loss = list()
for i in tqdm(num):
    f = open(log_path + epoch_fmt + str(i)).read()
    loss.append(float(f.split('loss:')[-1].split(', *')[0]))

f = f.split('*')[-1].split(':')[-1]
best_loss = float(f.split('[')[0])
best_epoch = int(f.split('[')[-1].split('/')[0])

plt.figure(figsize=(15, 10))
plt.grid(True)
title = "epoch_to_loss_" + ("re" if types == "real" else "se") + "_" + str(num_classes)
save_path = fig_path + "/" + title
plt.plot(num[::5], loss[::5], LineWidth=1)
plt.plot(best_epoch, best_loss, 'rs')
#plt.annotate('best loss', xy=(best_epoch, best_loss), xytext=(best_epoch, best_loss))
plt.xlabel('epoch', fontsize=18)
plt.ylabel('loss', fontsize=18)
plt.title(title, fontsize=28, fontweight=560)
plt.savefig(save_path + '.png')
#plt.show()

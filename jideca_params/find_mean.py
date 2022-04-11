import glob
import argparse
import pandas as pd

par = argparse.ArgumentParser()
par.add_argument("-d", "--dir", default="beta", choices=["beta", "gamma"],
                 type=str, help="Select directory (beta, gamma)")
args = par.parse_args()

evaluation_methods = ['ari', 'nmi', 'purity']
ari_best_result = dict()
nmi_best_result = dict()
purity_best_result = dict()

total = 0
for dirs in glob.glob(args.dir + '/*'):
    for em in evaluation_methods:
        with open(dirs + '/' + em + '/total_best_result.txt') as f:
            lines = f.read().splitlines()
            for i, line in enumerate(lines):
                if i == 0: continue
                line = line.split('=')[-1].split(':')
                k, v = line[0].strip(), line[-1].strip()
                if em == 'ari':
                    if k in ari_best_result:
                        ari_best_result[k] += float(v)
                    else:
                        ari_best_result[k] = float(v)
                elif em == 'nmi':
                    if k in nmi_best_result:
                        nmi_best_result[k] += float(v)
                    else:
                        nmi_best_result[k] = float(v)
                else:
                    if k in purity_best_result:
                        purity_best_result[k] += float(v.split('%')[0])
                    else:
                        purity_best_result[k] = float(v.split('%')[0])
    total += 1

for k, v in ari_best_result.items():
    ari_best_result[k] = round(v / total, 3)
for k, v in nmi_best_result.items():
    nmi_best_result[k] = round(v / total, 3)
for k, v in purity_best_result.items():
    purity_best_result[k] = round(v / total, 1)

print(ari_best_result)
print(nmi_best_result)
print(purity_best_result)

df_ari = pd.DataFrame(list(ari_best_result.items()), columns=['parameters', 'ari'])
df_nmi = pd.DataFrame(list(nmi_best_result.items()), columns=['parameters', 'nmi'])
df_purity = pd.DataFrame(list(purity_best_result.items()), columns=['parameters', 'purity'])


df_ari['simple'] = df_ari['parameters'].apply(lambda x: x.split('_')[1].split('r')[0][1:])
df_ari['simple'] = df_ari['simple'].apply(lambda x: float('0.' + x[1]) if x[0] == '0' else float(x))
df_ari['types'] = df_ari['parameters'].apply(lambda x:x.split('_')[1][-2:])

df_nmi['simple'] = df_nmi['parameters'].apply(lambda x:x.split('_')[1].split('r')[0][1:])
#df_nmi['simple'] = df_nmi['simple'].apply(lambda x: float('0.' + x[1]) if x[0] == '0' else float(x))
df_nmi['simple'] = df_nmi['simple'].apply(lambda x: '0.' + x[1] if x[0] == '0' else x)
df_nmi['types'] = df_nmi['parameters'].apply(lambda x:x.split('_')[1][-2:])

df_purity['simple'] = df_purity['parameters'].apply(lambda x:x.split('_')[1].split('r')[0][1:])
df_purity['simple'] = df_purity['simple'].apply(lambda x: float('0.' + x[1]) if x[0] == '0' else float(x))
df_purity['types'] = df_purity['parameters'].apply(lambda x:x.split('_')[1][-2:])


df_ari.to_csv(args.dir + '_ari_means.csv')
df_nmi.to_csv(args.dir + '_nmi_means.csv')
df_purity.to_csv(args.dir + '_purity_means.csv')

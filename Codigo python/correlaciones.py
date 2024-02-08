import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Info sobre heatmap
# https://medium.com/@szabo.bibor/how-to-create-a-seaborn-correlation-heatmap-in-python-834c0686b88e

df_interac_nt = pd.read_csv("nt e interacc.csv")
(df_interac_nt).head()

df_interac_nt_correlacion = df_interac_nt.corr()

sns.heatmap(df_interac_nt_correlacion, annot=True)
plt.show()

mask = np.triu(np.ones_like(df_interac_nt_correlacion, dtype=np.bool))
heatmap = sns.heatmap(
    df_interac_nt_correlacion, mask=mask, vmin=-1, vmax=0.50, annot=True
)
plt.show()

####################
df_interac_aa = pd.read_csv("aa e interacc.csv")
(df_interac_aa).head()

df_interac_aa_correlacion = df_interac_aa.corr()

sns.heatmap(df_interac_aa_correlacion, annot=True)
plt.show()

mask_1 = np.triu(np.ones_like(df_interac_aa_correlacion, dtype=np.bool))
heatmap = sns.heatmap(
    df_interac_aa_correlacion, mask=mask_1, vmin=-1, vmax=0.75, annot=True
)
plt.show()

####################
####################
# https://saturncloud.io/blog/how-to-list-highest-correlation-pairs-from-a-large-correlation-matrix-in-pandas/

## nt interac correlacion mas alta
# Stack the correlation matrix
stacked_corr_nt = df_interac_nt_correlacion.stack()

highest_corr_pairs_nt = stacked_corr_nt.nlargest(21)

# Print the highest correlation pairs
print(highest_corr_pairs_nt)

# save print to file
import sys

sys.stdout = open("randomfile.txt", "w")
print(highest_corr_pairs_nt)
sys.stdout.close()


## aa interac correlacion mas alta
# Stack the correlation matrix
stacked_corr_aa = df_interac_aa_correlacion.stack()

highest_corr_pairs_aa = stacked_corr_aa.nlargest(69)

# Print the highest correlation pairs
print(highest_corr_pairs_aa)

# save to csv to have complete results

highest_corr_pairs_aa.to_csv(
    r"F:\\Tesis_Maestria\\Processed Data\\13_01_oct_23_correlaciones\\log_corr_aa.csv"
)

############################################3

##correlaciones entre aa y nt

df_interac_nt_aa = pd.read_csv("aa y nt.csv")
(df_interac_nt_aa).head()

df_interac_aa_nt_correlacion = df_interac_nt_aa.corr()

mask_2 = np.triu(np.ones_like(df_interac_aa_nt_correlacion, dtype=np.bool))
heatmap = sns.heatmap(
    df_interac_aa_nt_correlacion, mask=mask_2, vmin=-1, vmax=0.75, annot=True
)
plt.show()

stacked_corr_aa_nt = df_interac_aa_nt_correlacion.stack()

highest_corr_pairs_aa_nt = stacked_corr_aa_nt.nlargest(69)

# Print the highest correlation pairs
print(highest_corr_pairs_aa_nt)

# save to csv to have complete results

highest_corr_pairs_aa_nt.to_csv(
    r"F:\\Tesis_Maestria\\Processed Data\\13_01_oct_23_correlaciones\\log_corr_aa_nt.csv"
)

# librerias necesarias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# loading file
total_monomers = pd.read_csv(
    "F:\\Tesis_Maestria\\Processed Data\\10_11_sep_23_conteo de interacciones aa y nt\\conteo total aa y nt_otro formato.csv"
)

total_monomers_tabla_2_columnas = pd.read_csv(
    "F:\\Tesis_Maestria\\Processed Data\\10_11_sep_23_conteo de interacciones aa y nt\\conteo total aa y nt.csv"
)

# valores estadisticos

total_monomers.describe()
total_monomers.head()
total_monomers_tabla_2_columnas.head()

# Graphs

## bar plots
monomers = total_monomers_tabla_2_columnas["MONOMER"]
num_toTal = total_monomers_tabla_2_columnas["TOTAL"]

plt.bar(monomers, num_toTal)
plt.show()

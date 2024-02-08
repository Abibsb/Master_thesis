# https://www.kaggle.com/code/abigailstricker/python-for-data-21-descriptive-statistics/edit

# librerias necesarias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# loading file
interacciones_norm_interactype = pd.read_csv(
    "F:\\Tesis_Maestria\\Processed Data\\09_09_sep_23_otras normalizaciones\\tabla full normalizado por HBOND Y VDW.csv"
)


###### valores usuales de estadistica
interacciones_norm_interactype.head()

interacciones_norm_interactype.mean()  # Get the mean of each column

interacciones_norm_interactype.mean(axis=1)  # Get the mean of each row

interacciones_norm_interactype.median()  # Get the median of each column

interacciones_norm_interactype.mode()

interacciones_norm_interactype.describe()


###### grafico de data + mean y median

# hbond
##densidad

interacciones_norm_interactype["Total HBOND"].plot(
    kind="density", figsize=(10, 10), xlim=(-1, 5)
)


plt.vlines(
    interacciones_norm_interactype["Total HBOND"].mean(),
    ymin=0,
    ymax=0.8,
    linewidth=5.0,  # Plot black line at mean
)

plt.vlines(
    interacciones_norm_interactype["Total HBOND"].median(),  # Plot red line at median
    ymin=0,
    ymax=0.8,
    linewidth=2.0,
    color="red",
)
plt.show()

##histograma
interacciones_norm_interactype["Total HBOND"].plot(
    kind="hist", figsize=(10, 10), xlim=(-1, 5)
)
plt.show()

## measures of spread

rango = max(interacciones_norm_interactype["Total HBOND"]) - min(
    interacciones_norm_interactype["Total HBOND"]
)
rango

five_num = [
    interacciones_norm_interactype["Total HBOND"].quantile(0),
    interacciones_norm_interactype["Total HBOND"].quantile(0.25),
    interacciones_norm_interactype["Total HBOND"].quantile(0.50),
    interacciones_norm_interactype["Total HBOND"].quantile(0.75),
    interacciones_norm_interactype["Total HBOND"].quantile(1),
]

five_num

### IQR
interacciones_norm_interactype["Total HBOND"].quantile(
    0.75
) - interacciones_norm_interactype["Total HBOND"].quantile(0.25)

### Boxploots IQR
interacciones_norm_interactype.boxplot(
    column="Total HBOND", return_type="axes", figsize=(8, 8)
)
plt.show()
plt.text(x=0.74, y=22.25, s="3rd Quartile")
plt.text(x=0.8, y=18.75, s="Median")
plt.text(x=0.75, y=15.5, s="1st Quartile")
plt.text(x=0.9, y=10, s="Min")
plt.text(x=0.9, y=33.5, s="Max")
plt.text(x=0.7, y=19.5, s="IQR", rotation=90, size=25)

### Variance
interacciones_norm_interactype["Total HBOND"].var()

### Standard deviation
interacciones_norm_interactype["Total HBOND"].std()

# Skewness and Kurtosis

## Now let's check the skewness of each of the distributions. Since skewness measures asymmetry, we'd expect to see low skewness for all of the distributions except the skewed one, because all the others are roughly symmetric:
interacciones_norm_interactype["Total HBOND"].skew()  # Check skewness

## As we can see from the output, the normally distributed data has a kurtosis near zero, the flat distribution has negative kurtosis and the two distributions with more data in the tails vs the center have higher kurtosis.
interacciones_norm_interactype["Total HBOND"].kurt()  # Check kurtosis

# VDW
##densidad

interacciones_norm_interactype["Total VDW"].plot(
    kind="density", figsize=(10, 10), xlim=(-1, 5)
)


plt.vlines(
    interacciones_norm_interactype["Total VDW"].mean(),
    ymin=0,
    ymax=0.8,
    linewidth=5.0,  # Plot black line at mean
)

plt.vlines(
    interacciones_norm_interactype["Total VDW"].median(),  # Plot red line at median
    ymin=0,
    ymax=0.8,
    linewidth=2.0,
    color="red",
)
plt.show()

##histograma
interacciones_norm_interactype["Total VDW"].plot(
    kind="hist", figsize=(10, 10), xlim=(-1, 5)
)
plt.show()

## measures of spread

rango = max(interacciones_norm_interactype["Total VDW"]) - min(
    interacciones_norm_interactype["Total VDW"]
)
rango

five_num = [
    interacciones_norm_interactype["Total VDW"].quantile(0),
    interacciones_norm_interactype["Total VDW"].quantile(0.25),
    interacciones_norm_interactype["Total VDW"].quantile(0.50),
    interacciones_norm_interactype["Total VDW"].quantile(0.75),
    interacciones_norm_interactype["Total VDW"].quantile(1),
]

five_num

### IQR
interacciones_norm_interactype["Total VDW"].quantile(
    0.75
) - interacciones_norm_interactype["Total VDW"].quantile(0.25)

### Boxploots IQR
interacciones_norm_interactype.boxplot(
    column="Total VDW", return_type="axes", figsize=(8, 8)
)
plt.show()
plt.text(x=0.74, y=22.25, s="3rd Quartile")
plt.text(x=0.8, y=18.75, s="Median")
plt.text(x=0.75, y=15.5, s="1st Quartile")
plt.text(x=0.9, y=10, s="Min")
plt.text(x=0.9, y=33.5, s="Max")
plt.text(x=0.7, y=19.5, s="IQR", rotation=90, size=25)

### Variance
interacciones_norm_interactype["Total VDW"].var()

### Standard deviation
interacciones_norm_interactype["Total VDW"].std()

# Skewness and Kurtosis

## Now let's check the skewness of each of the distributions. Since skewness measures asymmetry, we'd expect to see low skewness for all of the distributions except the skewed one, because all the others are roughly symmetric:
interacciones_norm_interactype["Total VDW"].skew()  # Check skewness

## As we can see from the output, the normally distributed data has a kurtosis near zero, the flat distribution has negative kurtosis and the two distributions with more data in the tails vs the center have higher kurtosis.
interacciones_norm_interactype["Total VDW"].kurt()  # Check kurtosis

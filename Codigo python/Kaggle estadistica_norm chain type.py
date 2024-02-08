# https://www.kaggle.com/code/abigailstricker/python-for-data-21-descriptive-statistics/edit

# librerias necesarias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# loading file
interacciones_norm_chaintype = pd.read_csv(
    "F:\\Tesis_Maestria\\Processed Data\\09_09_sep_23_otras normalizaciones\\tabla full normalizado por SC Y MC.csv"
)


###### valores usuales de estadistica
interacciones_norm_chaintype.head()

interacciones_norm_chaintype.mean()  # Get the mean of each column

interacciones_norm_chaintype.mean(axis=1)  # Get the mean of each row

interacciones_norm_chaintype.median()  # Get the median of each column

interacciones_norm_chaintype.mode()

interacciones_norm_chaintype.describe()


###### grafico de data + mean y median

# Main chain
##densidad

interacciones_norm_chaintype["Total MC"].plot(
    kind="density", figsize=(10, 10), xlim=(-1, 5)
)


plt.vlines(
    interacciones_norm_chaintype["Total MC"].mean(),
    ymin=0,
    ymax=0.8,
    linewidth=5.0,  # Plot black line at mean
)

plt.vlines(
    interacciones_norm_chaintype["Total MC"].median(),  # Plot red line at median
    ymin=0,
    ymax=0.8,
    linewidth=2.0,
    color="red",
)
plt.show()

##histograma
interacciones_norm_chaintype["Total MC"].plot(
    kind="hist", figsize=(10, 10), xlim=(-1, 5)
)
plt.show()

## measures of spread

rango = max(interacciones_norm_chaintype["Total MC"]) - min(
    interacciones_norm_chaintype["Total MC"]
)
rango

five_num = [
    interacciones_norm_chaintype["Total MC"].quantile(0),
    interacciones_norm_chaintype["Total MC"].quantile(0.25),
    interacciones_norm_chaintype["Total MC"].quantile(0.50),
    interacciones_norm_chaintype["Total MC"].quantile(0.75),
    interacciones_norm_chaintype["Total MC"].quantile(1),
]

five_num

### IQR
interacciones_norm_chaintype["Total MC"].quantile(0.75) - interacciones_norm_chaintype[
    "Total MC"
].quantile(0.25)

### Boxploots IQR
interacciones_norm_chaintype.boxplot(
    column="Total MC", return_type="axes", figsize=(8, 8)
)
plt.show()
plt.text(x=0.74, y=22.25, s="3rd Quartile")
plt.text(x=0.8, y=18.75, s="Median")
plt.text(x=0.75, y=15.5, s="1st Quartile")
plt.text(x=0.9, y=10, s="Min")
plt.text(x=0.9, y=33.5, s="Max")
plt.text(x=0.7, y=19.5, s="IQR", rotation=90, size=25)

### Variance
interacciones_norm_chaintype["Total MC"].var()

### Standard deviation
interacciones_norm_chaintype["Total MC"].std()

# Skewness and Kurtosis

## Now let's check the skewness of each of the distributions. Since skewness measures asymmetry, we'd expect to see low skewness for all of the distributions except the skewed one, because all the others are roughly symmetric:
interacciones_norm_chaintype["Total MC"].skew()  # Check skewness

## As we can see from the output, the normally distributed data has a kurtosis near zero, the flat distribution has negative kurtosis and the two distributions with more data in the tails vs the center have higher kurtosis.
interacciones_norm_chaintype["Total MC"].kurt()  # Check kurtosis

# Side chain
##densidad

interacciones_norm_chaintype["Total SD"].plot(
    kind="density", figsize=(10, 10), xlim=(-1, 5)
)


plt.vlines(
    interacciones_norm_chaintype["Total SD"].mean(),
    ymin=0,
    ymax=0.8,
    linewidth=5.0,  # Plot black line at mean
)

plt.vlines(
    interacciones_norm_chaintype["Total SD"].median(),  # Plot red line at median
    ymin=0,
    ymax=0.8,
    linewidth=2.0,
    color="red",
)
plt.show()

##histograma
interacciones_norm_chaintype["Total SD"].plot(
    kind="hist", figsize=(10, 10), xlim=(-1, 5)
)
plt.show()

## measures of spread

rango = max(interacciones_norm_chaintype["Total SD"]) - min(
    interacciones_norm_chaintype["Total SD"]
)
rango

five_num = [
    interacciones_norm_chaintype["Total SD"].quantile(0),
    interacciones_norm_chaintype["Total SD"].quantile(0.25),
    interacciones_norm_chaintype["Total SD"].quantile(0.50),
    interacciones_norm_chaintype["Total SD"].quantile(0.75),
    interacciones_norm_chaintype["Total SD"].quantile(1),
]

five_num

### IQR
interacciones_norm_chaintype["Total SD"].quantile(0.75) - interacciones_norm_chaintype[
    "Total SD"
].quantile(0.25)

### Boxploots IQR
interacciones_norm_chaintype.boxplot(
    column="Total SD", return_type="axes", figsize=(8, 8)
)
plt.show()
plt.text(x=0.74, y=22.25, s="3rd Quartile")
plt.text(x=0.8, y=18.75, s="Median")
plt.text(x=0.75, y=15.5, s="1st Quartile")
plt.text(x=0.9, y=10, s="Min")
plt.text(x=0.9, y=33.5, s="Max")
plt.text(x=0.7, y=19.5, s="IQR", rotation=90, size=25)

### Variance
interacciones_norm_chaintype["Total SD"].var()

### Standard deviation
interacciones_norm_chaintype["Total SD"].std()

# Skewness and Kurtosis

## Now let's check the skewness of each of the distributions. Since skewness measures asymmetry, we'd expect to see low skewness for all of the distributions except the skewed one, because all the others are roughly symmetric:
interacciones_norm_chaintype["Total SD"].skew()  # Check skewness

## As we can see from the output, the normally distributed data has a kurtosis near zero, the flat distribution has negative kurtosis and the two distributions with more data in the tails vs the center have higher kurtosis.
interacciones_norm_chaintype["Total SD"].kurt()  # Check kurtosis

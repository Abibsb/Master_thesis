# https://www.kaggle.com/code/abigailstricker/python-for-data-21-descriptive-statistics/edit

# librerias necesarias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# loading file
interacciones_normalizadas = pd.read_csv("F:\\Tesis_Maestria\\Processed Data\\07_26_jun_23_estadistica descrp\\estadistica_limpio.csv")


###### valores usuales de estadistica
interacciones_normalizadas.head()

interacciones_normalizadas.mean()  # Get the mean of each column

interacciones_normalizadas.mean(axis=1)  # Get the mean of each row

interacciones_normalizadas.median()  # Get the median of each column

interacciones_normalizadas.mode()

interacciones_normalizadas.describe()
interacciones_normalizadas.type()

###### grafico de data + mean y median

#hbond entre ligando y side chain

interacciones_normalizadas["HBOND_LIG_SC2 normal"].plot(kind="density", figsize=(10, 10), xlim=(-1, 5))


plt.vlines(
    interacciones_normalizadas["HBOND_LIG_SC2 normal"].mean(), ymin=0, ymax=0.8, linewidth=5.0  # Plot black line at mean
)

plt.vlines(
    interacciones_normalizadas["HBOND_LIG_SC2 normal"].median(),  # Plot red line at median
    ymin=0,
    ymax=0.8,
    linewidth=2.0,
    color="red",
)

#hbond entre ligando y main chain

interacciones_normalizadas["HBOND:LIG_MC3 normal"].plot(kind="density", figsize=(10, 10), xlim=(-1, 5))


plt.vlines(
    interacciones_normalizadas["HBOND:LIG_MC3 normal"].mean(), ymin=0, ymax=0.8, linewidth=5.0  # Plot black line at mean
)

plt.vlines(
    interacciones_normalizadas["HBOND:LIG_MC3 normal"].median(),  # Plot red line at median
    ymin=0,
    ymax=0.8,
    linewidth=2.0,
    color="red",
)

#hbond entre side chain y ligando

interacciones_normalizadas["HBOND:SC_LIG4 normal"].plot(kind="density", figsize=(10, 10), xlim=(-1, 5))


plt.vlines(
    interacciones_normalizadas["HBOND:SC_LIG4 normal"].mean(), ymin=0, ymax=0.8, linewidth=5.0  # Plot black line at mean
)

plt.vlines(
    interacciones_normalizadas["HBOND:SC_LIG4 normal"].median(),  # Plot red line at median
    ymin=0,
    ymax=0.8,
    linewidth=2.0,
    color="red",
)

#hbond entre main chain y ligando

interacciones_normalizadas["HBOND:MC_LIG5 normal"].plot(kind="density", figsize=(10, 10), xlim=(-1, 5))


plt.vlines(
    interacciones_normalizadas["HBOND:MC_LIG5 normal"].mean(), ymin=0, ymax=0.8, linewidth=5.0  # Plot black line at mean
)

plt.vlines(
    interacciones_normalizadas["HBOND:MC_LIG5 normal"].median(),  # Plot red line at median
    ymin=0,
    ymax=0.8,
    linewidth=2.0,
    color="red",
)

#vdw interac entre ligando y side chain

interacciones_normalizadas["VDW:LIG_SC6 normal"].plot(kind="density", figsize=(10, 10), xlim=(-1, 5))


plt.vlines(
    interacciones_normalizadas["VDW:LIG_SC6 normal"].mean(), ymin=0, ymax=0.8, linewidth=5.0  # Plot black line at mean
)

plt.vlines(
    interacciones_normalizadas["VDW:LIG_SC6 normal"].median(),  # Plot red line at median
    ymin=0,
    ymax=0.8,
    linewidth=2.0,
    color="red",
)

#vdw interac entre ligando y main chain

interacciones_normalizadas["VDW:LIG_MC7 normal"].plot(kind="density", figsize=(10, 10), xlim=(-1, 5))


plt.vlines(
    interacciones_normalizadas["VDW:LIG_MC7 normal"].mean(), ymin=0, ymax=0.8, linewidth=5.0  # Plot black line at mean
)

plt.vlines(
    interacciones_normalizadas["VDW:LIG_MC7 normal"].median(),  # Plot red line at median
    ymin=0,
    ymax=0.8,
    linewidth=2.0,
    color="red",
)

#vdw interac entre side chain y ligando

interacciones_normalizadas["VDW:SC_LIG8 normal"].plot(kind="density", figsize=(10, 10), xlim=(-1, 5))


plt.vlines(
    interacciones_normalizadas["VDW:SC_LIG8 normal"].mean(), ymin=0, ymax=0.8, linewidth=5.0  # Plot black line at mean
)

plt.vlines(
    interacciones_normalizadas["VDW:SC_LIG8 normal"].median(),  # Plot red line at median
    ymin=0,
    ymax=0.8,
    linewidth=2.0,
    color="red",
)

#vdw interac entre main chain y ligando

interacciones_normalizadas["VDW:MC_LIG9 normal"].plot(kind="density", figsize=(10, 10), xlim=(-1, 5))


plt.vlines(
    interacciones_normalizadas["VDW:MC_LIG9 normal"].mean(), ymin=0, ymax=0.8, linewidth=5.0  # Plot black line at mean
)

plt.vlines(
    interacciones_normalizadas["VDW:MC_LIG9 normal"].median(),  # Plot red line at median
    ymin=0,
    ymax=0.8,
    linewidth=2.0,
    color="red",
)

###### Measures of spread

#hbond entre ligando y side chain



rango=max(interacciones_normalizadas["HBOND_LIG_SC2 normal"]) - min(interacciones_normalizadas["HBOND_LIG_SC2 normal"])
rango

five_num = [
    interacciones_normalizadas["HBOND_LIG_SC2 normal"].quantile(0),
    interacciones_normalizadas["HBOND_LIG_SC2 normal"].quantile(0.25),
    interacciones_normalizadas["HBOND_LIG_SC2 normal"].quantile(0.50),
    interacciones_normalizadas["HBOND_LIG_SC2 normal"].quantile(0.75),
    interacciones_normalizadas["HBOND_LIG_SC2 normal"].quantile(1),
]

five_num

# IQR
interacciones_normalizadas["HBOND_LIG_SC2 normal"].quantile(0.75) - interacciones_normalizadas["HBOND_LIG_SC2 normal"].quantile(0.25)

# Boxploots IQR
interacciones_normalizadas.boxplot(column="HBOND_LIG_SC2 normal", return_type="axes", figsize=(8, 8))

plt.text(x=0.74, y=22.25, s="3rd Quartile")
plt.text(x=0.8, y=18.75, s="Median")
plt.text(x=0.75, y=15.5, s="1st Quartile")
plt.text(x=0.9, y=10, s="Min")
plt.text(x=0.9, y=33.5, s="Max")
plt.text(x=0.7, y=19.5, s="IQR", rotation=90, size=25)

# Variance
interacciones_normalizadas["HBOND_LIG_SC2 normal"].var()

# Standard deviation
interacciones_normalizadas["HBOND_LIG_SC2 normal"].std()


###### Skewness and Kurtosis

# Now let's check the skewness of each of the distributions. Since skewness measures asymmetry, we'd expect to see low skewness for all of the distributions except the skewed one, because all the others are roughly symmetric:
interacciones_normalizadas["HBOND_LIG_SC2 normal"].skew()  # Check skewness

# As we can see from the output, the normally distributed data has a kurtosis near zero, the flat distribution has negative kurtosis and the two distributions with more data in the tails vs the center have higher kurtosis.
interacciones_normalizadas["HBOND_LIG_SC2 normal"].kurt()  # Check kurtosis

#hbond entre ligando y main chain



rango=max(interacciones_normalizadas["HBOND_LIG_MC3 normal"] - min(interacciones_normalizadas["HBOND_LIG_MC3 normal"])
rango

five_num = [
    interacciones_normalizadas["HBOND_LIG_MC3 normal"].quantile(0),
    interacciones_normalizadas["HBOND_LIG_MC3 normal"].quantile(0.25),
    interacciones_normalizadas["HBOND_LIG_MC3 normal"].quantile(0.50),
    interacciones_normalizadas["HBOND_LIG_MC3 normal"].quantile(0.75),
    interacciones_normalizadas["HBOND_LIG_MC3 normal"].quantile(1),
]

five_num

# IQR
interacciones_normalizadas["HBOND_LIG_MC3 normal"].quantile(0.75) - interacciones_normalizadas["HBOND_LIG_MC3 normal"].quantile(0.25)

# Boxploots IQR
interacciones_normalizadas.boxplot(column="HBOND_LIG_MC3 normal", return_type="axes", figsize=(8, 8))

plt.text(x=0.74, y=22.25, s="3rd Quartile")
plt.text(x=0.8, y=18.75, s="Median")
plt.text(x=0.75, y=15.5, s="1st Quartile")
plt.text(x=0.9, y=10, s="Min")
plt.text(x=0.9, y=33.5, s="Max")
plt.text(x=0.7, y=19.5, s="IQR", rotation=90, size=25)

# Variance
interacciones_normalizadas["HBOND_LIG_MC3 normal"].var()

# Standard deviation
interacciones_normalizadas["HBOND_LIG_MC3 normal"].std()


###### Skewness and Kurtosis

# Now let's check the skewness of each of the distributions. Since skewness measures asymmetry, we'd expect to see low skewness for all of the distributions except the skewed one, because all the others are roughly symmetric:
interacciones_normalizadas["HBOND_LIG_MC3 normal"].skew()  # Check skewness

# As we can see from the output, the normally distributed data has a kurtosis near zero, the flat distribution has negative kurtosis and the two distributions with more data in the tails vs the center have higher kurtosis.
interacciones_normalizadas["HBOND_LIG_MC3 normal"].kurt()  # Check kurtosis


#hbond entre side chain y ligando



rango=max(interacciones_normalizadas["HBOND:SC_LIG4 normal"] - min(interacciones_normalizadas["HBOND:SC_LIG4 normal"]
rango

five_num = [
    interacciones_normalizadas["HBOND:SC_LIG4 normal"].quantile(0),
    interacciones_normalizadas["HBOND:SC_LIG4 normal"].quantile(0.25),
    interacciones_normalizadas["HBOND:SC_LIG4 normal"].quantile(0.50),
    interacciones_normalizadas["HBOND:SC_LIG4 normal"].quantile(0.75),
    interacciones_normalizadas["HBOND:SC_LIG4 normal"].quantile(1),
]

five_num

# IQR
interacciones_normalizadas["HBOND:SC_LIG4 normal"].quantile(0.75) - interacciones_normalizadas["HBOND:SC_LIG4 normal"].quantile(0.25)

# Boxploots IQR
interacciones_normalizadas.boxplot(column="HBOND:SC_LIG4 normal", return_type="axes", figsize=(8, 8))

plt.text(x=0.74, y=22.25, s="3rd Quartile")
plt.text(x=0.8, y=18.75, s="Median")
plt.text(x=0.75, y=15.5, s="1st Quartile")
plt.text(x=0.9, y=10, s="Min")
plt.text(x=0.9, y=33.5, s="Max")
plt.text(x=0.7, y=19.5, s="IQR", rotation=90, size=25)

# Variance
interacciones_normalizadas["HBOND:SC_LIG4 normal"].var()

# Standard deviation
interacciones_normalizadas["HBOND:SC_LIG4 normal"].std()


###### Skewness and Kurtosis

# Now let's check the skewness of each of the distributions. Since skewness measures asymmetry, we'd expect to see low skewness for all of the distributions except the skewed one, because all the others are roughly symmetric:
interacciones_normalizadas["HBOND:SC_LIG4 normal"].skew()  # Check skewness

# As we can see from the output, the normally distributed data has a kurtosis near zero, the flat distribution has negative kurtosis and the two distributions with more data in the tails vs the center have higher kurtosis.
interacciones_normalizadas["HBOND:SC_LIG4 normal"].kurt()  # Check kurtosis


#interacciones entre main chain y ligando

rango=max(interacciones_normalizadas["HBOND:MC_LIG5 normal"] - min(interacciones_normalizadas["HBOND:MC_LIG5 normal"]
rango

five_num = [
    interacciones_normalizadas["HBOND:MC_LIG5 normal"].quantile(0),
    interacciones_normalizadas["HBOND:MC_LIG5 normal"].quantile(0.25),
    interacciones_normalizadas["HBOND:MC_LIG5 normal"].quantile(0.50),
    interacciones_normalizadas["HBOND:MC_LIG5 normal"].quantile(0.75),
    interacciones_normalizadas["HBOND:MC_LIG5 normal"].quantile(1),
]

five_num

# IQR
interacciones_normalizadas["HBOND:MC_LIG5 normal"].quantile(0.75) - interacciones_normalizadas["HBOND:MC_LIG5 normal"].quantile(0.25)

# Boxploots IQR
interacciones_normalizadas.boxplot(column="HBOND:MC_LIG5 normal", return_type="axes", figsize=(8, 8))

plt.text(x=0.74, y=22.25, s="3rd Quartile")
plt.text(x=0.8, y=18.75, s="Median")
plt.text(x=0.75, y=15.5, s="1st Quartile")
plt.text(x=0.9, y=10, s="Min")
plt.text(x=0.9, y=33.5, s="Max")
plt.text(x=0.7, y=19.5, s="IQR", rotation=90, size=25)

# Variance
interacciones_normalizadas["HBOND:MC_LIG5 normal"].var()

# Standard deviation
interacciones_normalizadas["HBOND:MC_LIG5 normal"].std()


###### Skewness and Kurtosis

# Now let's check the skewness of each of the distributions. Since skewness measures asymmetry, we'd expect to see low skewness for all of the distributions except the skewed one, because all the others are roughly symmetric:
interacciones_normalizadas["HBOND:MC_LIG5 normal"].skew()  # Check skewness

# As we can see from the output, the normally distributed data has a kurtosis near zero, the flat distribution has negative kurtosis and the two distributions with more data in the tails vs the center have higher kurtosis.
interacciones_normalizadas["HBOND:MC_LIG5 normal"].kurt()  # Check kurtosis


#interacciones entre vdw ligando y side chain
rango=max(interacciones_normalizadas["VDW:LIG_SC6 normal"] - min(interacciones_normalizadas["VDW:LIG_SC6 normal"]
rango

five_num = [
    interacciones_normalizadas["VDW:LIG_SC6 normal"].quantile(0),
    interacciones_normalizadas["VDW:LIG_SC6 normal"].quantile(0.25),
    interacciones_normalizadas["VDW:LIG_SC6 normal"].quantile(0.50),
    interacciones_normalizadas["VDW:LIG_SC6 normal"].quantile(0.75),
    interacciones_normalizadas["VDW:LIG_SC6 normal"].quantile(1),
]

five_num

# IQR
interacciones_normalizadas["VDW:LIG_SC6 normal"].quantile(0.75) - interacciones_normalizadas["VDW:LIG_SC6 normal"].quantile(0.25)

# Boxploots IQR
interacciones_normalizadas.boxplot(column="VDW:LIG_SC6 normal", return_type="axes", figsize=(8, 8))

plt.text(x=0.74, y=22.25, s="3rd Quartile")
plt.text(x=0.8, y=18.75, s="Median")
plt.text(x=0.75, y=15.5, s="1st Quartile")
plt.text(x=0.9, y=10, s="Min")
plt.text(x=0.9, y=33.5, s="Max")
plt.text(x=0.7, y=19.5, s="IQR", rotation=90, size=25)

# Variance
interacciones_normalizadas["VDW:LIG_SC6 normal"].var()

# Standard deviation
interacciones_normalizadas["VDW:LIG_SC6 normal"].std()


###### Skewness and Kurtosis

# Now let's check the skewness of each of the distributions. Since skewness measures asymmetry, we'd expect to see low skewness for all of the distributions except the skewed one, because all the others are roughly symmetric:
interacciones_normalizadas["VDW:LIG_SC6 normal"].skew()  # Check skewness

# As we can see from the output, the normally distributed data has a kurtosis near zero, the flat distribution has negative kurtosis and the two distributions with more data in the tails vs the center have higher kurtosis.
interacciones_normalizadas["VDW:LIG_SC6 normal"].kurt()  # Check kurtosis

#interacciones entre vdw ligando y main chain
rango=max(interacciones_normalizadas["VDW:LIG_MC7 normal"] - min(interacciones_normalizadas["VDW:LIG_MC7 normal"]
rango

five_num = [
    interacciones_normalizadas["VDW:LIG_MC7 normal"].quantile(0),
    interacciones_normalizadas["VDW:LIG_MC7 normal"].quantile(0.25),
    interacciones_normalizadas["VDW:LIG_MC7 normal"].quantile(0.50),
    interacciones_normalizadas["VDW:LIG_MC7 normal"].quantile(0.75),
    interacciones_normalizadas["VDW:LIG_MC7 normal"].quantile(1),
]

five_num

# IQR
interacciones_normalizadas["VDW:LIG_MC7 normal"].quantile(0.75) - interacciones_normalizadas["VDW:LIG_MC7 normal"].quantile(0.25)

# Boxploots IQR
interacciones_normalizadas.boxplot(column="VDW:LIG_MC7 normal", return_type="axes", figsize=(8, 8))

plt.text(x=0.74, y=22.25, s="3rd Quartile")
plt.text(x=0.8, y=18.75, s="Median")
plt.text(x=0.75, y=15.5, s="1st Quartile")
plt.text(x=0.9, y=10, s="Min")
plt.text(x=0.9, y=33.5, s="Max")
plt.text(x=0.7, y=19.5, s="IQR", rotation=90, size=25)

# Variance
interacciones_normalizadas["VDW:LIG_MC7 normal"].var()

# Standard deviation
interacciones_normalizadas["VDW:LIG_MC7 normal"].std()


###### Skewness and Kurtosis

# Now let's check the skewness of each of the distributions. Since skewness measures asymmetry, we'd expect to see low skewness for all of the distributions except the skewed one, because all the others are roughly symmetric:
interacciones_normalizadas["VDW:LIG_MC7 normal"].skew()  # Check skewness

# As we can see from the output, the normally distributed data has a kurtosis near zero, the flat distribution has negative kurtosis and the two distributions with more data in the tails vs the center have higher kurtosis.
interacciones_normalizadas["VDW:LIG_MC7 normal"].kurt()  # Check kurtosis



#interacciones entre vdw side chain y ligando
rango=max(interacciones_normalizadas["VDW:SC_LIG8 normal"] - min(interacciones_normalizadas["VDW:SC_LIG8 normal"]
rango

five_num = [
    interacciones_normalizadas["VDW:SC_LIG8 normal"].quantile(0),
    interacciones_normalizadas["VDW:SC_LIG8 normal"].quantile(0.25),
    interacciones_normalizadas["VDW:SC_LIG8 normal"].quantile(0.50),
    interacciones_normalizadas["VDW:SC_LIG8 normal"].quantile(0.75),
    interacciones_normalizadas["VDW:SC_LIG8 normal"].quantile(1),
]

five_num

# IQR
interacciones_normalizadas["VDW:SC_LIG8 normal"].quantile(0.75) - interacciones_normalizadas["VDW:SC_LIG8 normal"].quantile(0.25)

# Boxploots IQR
interacciones_normalizadas.boxplot(column="VDW:SC_LIG8 normal", return_type="axes", figsize=(8, 8))

plt.text(x=0.74, y=22.25, s="3rd Quartile")
plt.text(x=0.8, y=18.75, s="Median")
plt.text(x=0.75, y=15.5, s="1st Quartile")
plt.text(x=0.9, y=10, s="Min")
plt.text(x=0.9, y=33.5, s="Max")
plt.text(x=0.7, y=19.5, s="IQR", rotation=90, size=25)

# Variance
interacciones_normalizadas["VDW:SC_LIG8 normal"].var()

# Standard deviation
interacciones_normalizadas["VDW:SC_LIG8 normal"].std()


###### Skewness and Kurtosis

# Now let's check the skewness of each of the distributions. Since skewness measures asymmetry, we'd expect to see low skewness for all of the distributions except the skewed one, because all the others are roughly symmetric:
interacciones_normalizadas["VDW:SC_LIG8 normal"].skew()  # Check skewness

# As we can see from the output, the normally distributed data has a kurtosis near zero, the flat distribution has negative kurtosis and the two distributions with more data in the tails vs the center have higher kurtosis.
interacciones_normalizadas["VDW:SC_LIG8 normal"].kurt()  # Check kurtosis


#interacciones entre vdw main chain y ligando
rango=max(interacciones_normalizadas["VDW:MC_LIG9 normal"] - min(interacciones_normalizadas["VDW:MC_LIG9 normal"]
rango

five_num = [
    interacciones_normalizadas["VDW:MC_LIG9 normal"].quantile(0),
    interacciones_normalizadas["VDW:MC_LIG9 normal"].quantile(0.25),
    interacciones_normalizadas["VDW:MC_LIG9 normal"].quantile(0.50),
    interacciones_normalizadas["VDW:MC_LIG9 normal"].quantile(0.75),
    interacciones_normalizadas["VDW:MC_LIG9 normal"].quantile(1),
]

five_num

# IQR
interacciones_normalizadas["VDW:MC_LIG9 normal"].quantile(0.75) - interacciones_normalizadas["VDW:MC_LIG9 normal"].quantile(0.25)

# Boxploots IQR
interacciones_normalizadas.boxplot(column="VDW:MC_LIG9 normal", return_type="axes", figsize=(8, 8))

plt.text(x=0.74, y=22.25, s="3rd Quartile")
plt.text(x=0.8, y=18.75, s="Median")
plt.text(x=0.75, y=15.5, s="1st Quartile")
plt.text(x=0.9, y=10, s="Min")
plt.text(x=0.9, y=33.5, s="Max")
plt.text(x=0.7, y=19.5, s="IQR", rotation=90, size=25)

# Variance
interacciones_normalizadas["VDW:MC_LIG9 normal"].var()

# Standard deviation
interacciones_normalizadas["VDW:MC_LIG9 normal"].std()


###### Skewness and Kurtosis

# Now let's check the skewness of each of the distributions. Since skewness measures asymmetry, we'd expect to see low skewness for all of the distributions except the skewed one, because all the others are roughly symmetric:
interacciones_normalizadas["VDW:MC_LIG9 normal"].skew()  # Check skewness

# As we can see from the output, the normally distributed data has a kurtosis near zero, the flat distribution has negative kurtosis and the two distributions with more data in the tails vs the center have higher kurtosis.
interacciones_normalizadas["VDW:MC_LIG9 normal"].kurt()  # Check kurtosis



# descriptive statistics - correlation
# https://dipankarmedh1.medium.com/descriptive-statistics-in-python-2f6f725739b1

# Correlation between features
df_corr = df.corr()
df_corr

plt.figure(figsize=(15, 15))
sns.heatmap(df_corr, vmin=-1, vmax=+1, annot=True)

# Normal distribution
# Plotting distribution of all the numerical features of the dataset using the seaborn distplot function.

numberical_features = df.select_dtypes(exclude=[np.object])
for i in numberical_features.columns:
    plt.figure(figsize=(9, 7))
    sns.distplot(numberical_features[i])
    plt.show()

# Box-cox
# Box Cox is a transformation method that transforms non-normal dependent variables in the data to a normal shape.

from scipy import stats

fitted_data, fitted_lambda = stats.boxcox(df["Annual_HH_Income"])

fig, ax = plt.subplots(1, 2)

sns.distplot(
    df["Annual_HH_Income"],
    hist=False,
    kde=True,
    kde_kws={"shade": True, "linewidth": 2},
    label="Non-Normal",
    color="yellow",
    ax=ax[0],
)

sns.distplot(
    fitted_data,
    hist=False,
    kde=True,
    kde_kws={"shade": True, "linewidth": 2},
    label="Normal",
    color="orange",
    ax=ax[1],
)

plt.legend(loc="upper right")

fig.set_figheight(5)
fig.set_figwidth(10)

print(f"Lambda value used for Transformation: {fitted_lambda}")

# https://github.com/Dipankar-Medhi/Descriptive_stats/blob/master/descriptive_stats.ipynb

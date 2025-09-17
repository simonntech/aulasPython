import seaborn as sns
import matplotlib.pyplot as plt

df_tips = sns.load_dataset('tips')

fig, ax = plt.subplots(1,3, figsize=(15,5))

sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[0])

sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[1], estimator=sum)

sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[2], estimator=len)

plt.show()
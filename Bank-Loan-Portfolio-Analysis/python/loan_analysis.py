import pandas as pd

df = pd.read_csv("dataset/loan.csv")

print(df.head())

print(df.columns)
print(df.isnull().sum())
print(df['loan_status'].value_counts())
df = df[['loan_amnt',
         'term',
         'int_rate',
         'installment',
         'grade',
         'emp_length',
         'home_ownership',
         'annual_inc',
         'loan_status']]

print(df.head())
df = df.dropna()

print(df.shape)

import seaborn as sns
import matplotlib.pyplot as plt

import seaborn as sns
import matplotlib.pyplot as plt

sns.countplot(x='loan_status', data=df)
plt.xticks(rotation=45)
plt.show()

sns.boxplot(x='loan_status', y='annual_inc', data=df)
plt.xticks(rotation=45)
plt.show()

sns.boxplot(x='loan_status', y='loan_amnt', data=df)
plt.xticks(rotation=45)
plt.show()

sns.countplot(x='grade', hue='loan_status', data=df)
plt.show()

df.to_csv("dataset/clean_loan.csv", index=False)
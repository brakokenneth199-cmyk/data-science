import numpy as np
import pandas as pd
mydata = pd.read_csv('CardioGoodFitness.csv')
mydata.head()
mydata.describe(include="all")
mydata.info()
import matplotlib.pyplot as plt

mydata.hist(figsize=(20,30))
import seaborn as sns

sns.boxplot(x="Gender", y="Age", data=mydata)
pd.crosstab(mydata['Product'],mydata['Gender'] )
pd.crosstab(mydata['Product'],mydata['MaritalStatus'] )
sns.countplot(x="Product", hue="Gender", data=mydata)
pd.pivot_table(mydata, index=['Product', 'Gender'],
                     columns=[ 'MaritalStatus'], aggfunc=len)
pd.pivot_table(mydata,'Income', index=['Product', 'Gender'],
                     columns=[ 'MaritalStatus'])
pd.pivot_table(mydata,'Miles', index=['Product', 'Gender'],
                     columns=[ 'MaritalStatus'])
sns.pairplot(mydata)
mydata['Age'].std()
mydata['Age'].mean()
sns.distplot(mydata['Age'])
mydata.hist(by='Gender',column = 'Age')
mydata.hist(by='Gender',column = 'Income')
mydata.hist(by='Gender',column = 'Miles')
mydata.hist(by='Product',column = 'Miles', figsize=(20,30))
corr = mydata.corr()
corr
sns.heatmap(corr, annot=True)
# -*- coding: utf-8 -*-
"""OlympicsXMachineLearning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1l6UVTiuCJAPVVMiTfKO8mVABiMQqWyan
"""

from google.colab import auth
auth.authenticate_user()
import gspread
from oauth2client.client import GoogleCredentials
gc = gspread.authorize(GoogleCredentials.get_application_default())
import pandas as pd
import matplotlib.pyplot as plt

#Olympics data
wb = gc.open_by_url('https://docs.google.com/spreadsheets/d/1SuHeBfBeMbvPIQwHQUnvNCpOUrCLrjGAhKExaLREHYA/edit#gid=709589584')

sheet = wb.worksheet('data1') #change this sheet name for a new dataset
data = sheet.get_all_values()


df = pd.DataFrame(data)


df.columns = df.iloc[0]
df = df.iloc[1:]


df.head()

df.dtypes

# Olympics data

df['Age'] = df['Age'].apply(lambda x: 'NaN' if x == 'NA' else x)
df['Height'] = df['Height'].apply(lambda x: 'NaN' if x == 'NA' else x)
df['Weight'] = df['Weight'].apply(lambda x: 'NaN' if x == 'NA' else x)

# Data Types
new_df = {
    'Name': df['Name'].astype(str),
    'Sex': df['Sex'].astype(str),
    'Age': df['Age'].astype(float),
    'Height': df['Height'].astype(float),
    'Weight': df['Weight'].astype(float),
    'Team': df['Team'].astype(str),
    'NOC': df['NOC'].astype(str),
    'Games': df['Games'].astype(str),
    'Year': df['Year'].astype(int),
    'Season': df['Season'].astype(str),
    'City': df['City'].astype(str),
    'Sport': df['Sport'].astype(str),
    'Event': df['Event'].astype(str),
    'Medal': df['Medal'].astype(str)
}
df

olympics_df = pd.DataFrame(new_df)
olympics_df['Medal'] = df['Medal'].apply(lambda x: '0' if x == 'NA' else x)
olympics_df['Medal'] = olympics_df['Medal'].apply(lambda x: '3' if x == 'Gold' else x)
olympics_df['Medal'] = olympics_df['Medal'].apply(lambda x: '2' if x == 'Silver' else x)
olympics_df['Medal'] = olympics_df['Medal'].apply(lambda x: '1' if x == 'Bronze' else x)
olympics_df['Sex'] = olympics_df['Sex'].apply(lambda x: '1' if x == 'M' else x)
olympics_df['Sex'] = olympics_df['Sex'].apply(lambda x: '0' if x == 'F' else x)


bronze_test = 0
for i in olympics_df["Medal"]:
  if (i == '1'):
    bronze_test += 1
print (bronze_test)

olympics_df['Medal'] = olympics_df['Medal'].astype("float64")
olympics_df['Sex'] = olympics_df['Sex'].astype("float64")
olympics_df['Year'] = olympics_df['Year'].astype("float64")
df=df.dropna()
olympics_df['Height'] = df['Height'].astype("float64")
olympics_df['Weight'] = df['Weight'].astype("float64")
olympics_df = olympics_df.dropna()
olympics_df.head()

olympics_df.dtypes

olympics_df['Name'].describe()

olympics_df['Sex'].describe()

olympics_df['Age'].describe()

olympics_df['Height'].describe()

olympics_df['Weight'].describe()

import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
data = np.random.rand(4, 6)
heat_map = sb.heatmap(data)
plt.show()

plt.scatter(olympics_df['Medal'], olympics_df['Year'])
plt.xlabel('Medal', fontsize=14)
plt.ylabel('Year', fontsize=14)
plt.show()

plt.scatter(olympics_df['Sex'], olympics_df['Medal'])
plt.xlabel('Sex', fontsize=14)
plt.ylabel('Medal', fontsize=14)
plt.show()

plt.scatter(olympics_df['Medal'], olympics_df['Height'])
plt.xlabel('Medal', fontsize=14)
plt.ylabel('Height', fontsize=14)
plt.show()

plt.scatter(olympics_df['Medal'], olympics_df['Weight'])
plt.xlabel('Medal', fontsize=14)
plt.ylabel('Weight', fontsize=14)
plt.show()

from scipy import stats
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn import datasets
from sklearn.model_selection import train_test_split

olympics_df = olympics_df.dropna()
x = olympics_df[['Height','Weight','Age']]



y = olympics_df["Medal"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB

#Naive Bayes
model = GaussianNB()

# Fit the model with our training data
model.fit(x_train.to_numpy(),y_train.to_numpy())

# Use the model to make predictions using our testing input data
y_pred = model.predict(x_test.to_numpy())

# Calculate the accuracy of the model as a percent
accuracy = accuracy_score(y_test.to_numpy(),y_pred)*100
test_values = [[176.9,72.8,26.10]]
print(model.predict(test_values))
accuracy

# Import necessary package
from sklearn import svm

# Set input data (x) and target for prediction (y)
# I wrote this
x = olympics_df[['Height','Weight','Age','Sex']]
y = olympics_df[['Medal']]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)

# SVM
model = svm.LinearSVC()
model.fit(x_train,y_train)

# Use the model to make predictions using our testing input data
y_pred = model.predict(x_test)

# Calculate the accuracy of the model as a percent
accuracy = accuracy_score(y_test,y_pred)*100
accuracy

# Import necessary package
from sklearn.tree import DecisionTreeClassifier

# Set input data (x) and target for prediction (y)
# I wrote this
x = olympics_df[['Height','Weight']]
y = olympics_df[['Sex']]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.7)

#Decision Tree
model = DecisionTreeClassifier(criterion='entropy',random_state=0) 
model.fit(x_train,y_train)

# Use the model to make predictions using our testing input data
y_pred = model.predict(x_test)

# Calculate the accuracy of the model as a percent
accuracy = accuracy_score(y_test,y_pred)*100
accuracy

# Import necessary package
from sklearn.neural_network import MLPClassifier

# Set input data (x) and target for prediction (y)
# I wrote this
x = olympics_df[['Height','Weight','Age']]
y = olympics_df[['Medal']]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)

#Neural Network
model = MLPClassifier(hidden_layer_sizes=(8,8,8), activation='relu', solver='adam', max_iter=500)
model.fit(x_train,y_train)

# Use the model to make predictions using our testing input data
y_pred = model.predict(x_test)

# Calculate the accuracy of the model as a percent
accuracy = accuracy_score(y_test,y_pred)*100

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

x = olympics_df[['Height','Weight']]
y = olympics_df[['Sex']]
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.20)
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
regressor = RandomForestClassifier(n_estimators=20, random_state=0)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print(accuracy_score(y_test, y_pred))
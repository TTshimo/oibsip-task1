# -*- coding: utf-8 -*-
"""oibsip-task1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-lQXDSEwR7DQao88aw-Qpc0QA-2xPiIa

# **IMPORTING THE NECESSARY LIBRARIES**
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

"""# **LOADING THE DATAFRAME**

1. Loading the csv file
"""

dataset = 'Iris.csv'
print(dataset + ' read into the program!')

"""2. Loading the dataframe with Pandas"""

my_data = pd.read_csv(dataset)
print(my_data.head(5))

"""# **DATA PREPROCESSING**

**1. Dataframe Exploration**
"""

my_data.describe()

my_data.info()

"""**2. Data Cleaning**

2.1 Checking for duplicates
"""

print(my_data.duplicated().sum())

"""2.2 Checking for missing values"""

print(my_data.isnull().sum())

"""# **PREPARING FOR MODEL ENGINEERING**

1. Label Encoding
"""

label_mapping = {
    'Setosa': 0,
    'Versicolor': 1,
    'Virginica': 2
    }

label_encoder = LabelEncoder()
label_encoder.fit(my_data['Species'])
my_data['Species'] = label_encoder.transform(my_data['Species'])

"""2. Data splitting"""

X = my_data.drop('Species', axis=1)
y = my_data['Species']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

"""# **MODEL ENGINEERING**"""

#Random Forest Classifier
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)

#Training
rf_model.fit(X_train, y_train)

#Prediction making
y_pred = rf_model.predict(X_test)

#Evaluation
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print("\nClassification Report: " ,"\n", classification_report(y_test, y_pred), "\nConfusion Matrix: ", "\n", confusion_matrix(y_test, y_pred))

"""# **TESTING**"""

def get_user_input():
    input_data = {
        'Id': 0,
        'SepalLengthCm': float(input("Enter Sepal Length : ")),
        'SepalWidthCm': float(input("Enter Sepal Width : ")),
        'PetalLengthCm': float(input("Enter Petal Length : ")),
        'PetalWidthCm': float(input("Enter Petal Width : "))
    }
    return pd.DataFrame(input_data, index=[0])

def predict_flower(user_data, model, label_encoder):
    user_prediction = model.predict(user_data)
    decoded_prediction = label_encoder.inverse_transform(user_prediction)
    return decoded_prediction[0]

user_data = get_user_input()
predict_species = predict_flower(user_data, rf_model, label_encoder)
print("Predicted Flower Species:", predict_species)
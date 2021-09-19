import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import seaborn as sns
data = pd.read_csv('Crop_recommendation.csv')
X = data.drop('label' ,axis =1)

y = data['label']
from sklearn.model_selection import train_test_split
x_train1,x_test1,y_train1,y_test1 = train_test_split(X,y,test_size = 0.2, random_state=42)
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier()
rfc.fit(x_train1, y_train1)


pickle.dump(rfc, open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))
print(model.predict([[90,42,43,20.879744,82.002744,6.502985,202.935536]]))
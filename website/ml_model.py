import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression



data = pd.read_csv('test data/linear regression test data.csv')
x = data['X']
y = data['Y']
x_train,x_test,y_train,y_test = train_test_split(x,y, test_size=0.5, random_state=20)
x_train = np.array(x_train).reshape(-1,1)
x_test = np.array(x_test).reshape(-1,1)
linear_model = LinearRegression()
linear_model.fit(x_train, y_train)
y_pre = linear_model.predict(x_test)
print(linear_model.score(x_test,y_test))
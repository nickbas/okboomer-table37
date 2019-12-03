import boto3 
import botocore 
import pandas as pd 
from sagemaker import get_execution_role
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import matplotlib.pyplot as plt  
from sklearn.model_selection import train_test_split
​
role = get_execution_role() 
​
bucket = 'sagemaker-buildingheights' 
data_key = 'DC_Buildings_Footprint_4326_test_cleaned_v2.csv' 
data_location = 's3://{}/{}'.format(bucket, data_key) 
​
#pd.read_csv(data_location, low_memory=False, nrows=100)
dataset = pd.read_csv(data_location, low_memory=False, nrows=1000)
dataset.shape
dataset.plot(x='Shape_Area', y='ALTITUDE_M', style='o')  
plt.title('Shape_Area vs Altitude')  
plt.xlabel('Shape_Area')  
plt.ylabel('Altitude')  
plt.show()
​
X = dataset['Shape_Area'].values.reshape(-1,1)
y = dataset['ALTITUDE_M'].values.reshape(-1,1)
​
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
​
regressor = LinearRegression()  
regressor.fit(X_train, y_train) #training the algorithm
​
#To retrieve the intercept:
#print(regressor.intercept_)
#For retrieving the slope:
#print(regressor.coef_)
​
y_pred = regressor.predict(X_test)
​
df = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})
df

#importing the required libraries
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt 

def attribute_data_entropy(attribute_name,df):
	data=[]
	for i in range(3):
		a=df[df[attribute_name] == i][df[df[attribute_name] == i]["Play"] == 1]["Play"].size
		b=df[df[attribute_name] == i][df[df[attribute_name] == i]["Play"] == 0]["Play"].size
		data.append([a,b])
	return data

#Dictionary generation
def generate_dict(df):
	headers=list(df)
	values={}
	for header in headers:
		values[header]=[]
		for val in df[header]:
			if val not in values[header]:
				values[header].append(val)
	return values

#Calculating the information gain
def InformartionGain(p,n):
	if p==0 or n==0:
		return 0
	elif p==n:
		return 1
	else:
		return (((-p/(p+n))*math.log2(p/(p+n)))-((n/(p+n))*math.log2(n/(p+n))))


#Reading the data
df=pd.read_csv("data.csv")
#df.info()
#Making a dictionary out of the data frame
values_dict=generate_dict(df)
print(values_dict)
print("%.2f" % InformartionGain(3,3))

#Organizing the data
df['Play'],play=pd.factorize(df['Play'])
print(play)
print(df['Play'].unique())

df['Outlook'],outlook=pd.factorize(df['Outlook'])
print(outlook)
print(df['Outlook'].unique())

df['Temperature'],temp=pd.factorize(df['Temperature'])
print(temp)
print(df['Temperature'].unique())

df['Humidity'],humidity=pd.factorize(df['Humidity'])
print(humidity)
print(df['Humidity'].unique())

df['Wind'],wind=pd.factorize(df['Wind'])
print(wind)
print(df['Wind'].unique())

print("Positive and Negative values of Outlook\n",attribute_data_entropy("Outlook",df))
print("Positive and Negative values of Temperature\n",attribute_data_entropy("Temperature",df))
print("Positive and Negative values of Humidity\n",attribute_data_entropy("Humidity",df))
print("Positive and Negative values of Wind\n",attribute_data_entropy("Wind",df))
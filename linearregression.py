import pandas as pd  
import matplotlib.pyplot as plt
import numpy as np

def computeCost( X, y, thetha): #Cost func
    temp = np.dot(X,thetha)-y
    return np.sum(np.power(temp,2))/2*m

def gradientDescent( X, y, thetha, alpha, iterations):
    for _ in range(iterations):
        temp = np.dot(X,thetha) - y
        temp = np.dot(X.T,temp)
        thetha = thetha - (alpha/m) * temp
    return thetha

data = pd.read_csv("data2.csv")#Reading file

X = data.iloc[:,0] #first column
y = data.iloc[:,1]  #second column
m = len(y) #length of data

#plotting data
plt.scatter( X, y, color = "b", marker = "*")
plt.xlabel("population in 10,000's")
plt.ylabel("Profit in $10,000's")
plt.show()

X = X[:,np.newaxis]
y = y[:,np.newaxis]
thetha = np.zeros([2,1])
iterations = 1500
alpha = 0.01
ones = np.ones((m,1))
X = np.hstack((ones,X))

J = computeCost(X, y, thetha) #Computing cost

thetha = gradientDescent( X, y, thetha, alpha, iterations) #Finding optimal params
print("Theta0:", thetha[0])
print("Theta1:", thetha[1])

J = computeCost( X, y, thetha) #Computing cost
#print((J))

plt.scatter( X[:,1], y, color = "b", marker = "*")
plt.xlabel("population in 10,000's")
plt.ylabel("Profit in $10,000's")
plt.plot(X[:,1],np.dot(X,thetha))
plt.show()

X_input = float(input("Enter the value for which prediction is needed:"))

Prediction = thetha[0] + (thetha[1] * X_input)
print("Predicted value:", Prediction)
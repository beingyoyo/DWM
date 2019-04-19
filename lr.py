import statistics

number_of_inputs = int(input("Enter no. of inputs:"))
x, y = [], []

for i in range(0, number_of_inputs):
	xi = int(input("Enter x%d:"%(i+1)))
	yi = int(input("Enter y%d:"%(i+1)))
	x.append(xi)
	y.append(yi)

xmean, ymean = statistics.mean(x), statistics.mean(y)

xx, yy, xx2, xy = [], [], [], []

for i in range(0, number_of_inputs):
	a, b = x[i] - xmean, y[i] - ymean
	c, d = a ** 2, a * b
	xx.append(a)
	yy.append(b)
	xx2.append(c)
	xy.append(d)

b1 = sum(xy)/sum(xx2)
b0 = ymean - b1*xmean
xpred = int(input("Enter value of x for which y is needed:"))

ypred = b0 + b1*xpred
print("Prediction is: %.2f"%(ypred))
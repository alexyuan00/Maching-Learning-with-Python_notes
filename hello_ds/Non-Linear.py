import numpy as np 
import matplotlib.pyplot as ply 
%matplotlib inline

# models a linear relation between a dependent variable y and independent variable x. 
# It had a simple equation, of degree 1, for example y = 2*(x) + 3.

x = np.arange(-5.0, 5.0, 0.1)
y = 2*(x) + 3
y_noise = 2*np.random.normal(size=x.size) 
ydata = y + y_noise
# plt.figure(figsize=(8,6))
plt.plot(x, ydata, 'bo')
plt.plot(x,y, 'r')
plt.ylabel('Dependent Variable')
plt.xlabel('Indepdendent Variable')
plt.show()

x = np.arange(-5.0, 5.0, 0.1)
##You can adjust the slope and intercept to verify the changes in the graph
y = 1*(x**3) + 1*(x**2) + 1*x + 3
y_noise = 20 * np.random.normal(size=x.size)
ydata = y + y_noise
plt.plot(x, ydata,  'bo')
plt.plot(x,y, 'r') 
plt.ylabel('Dependent Variable')
plt.xlabel('Indepdendent Variable')
plt.show()
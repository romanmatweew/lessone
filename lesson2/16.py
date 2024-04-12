import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib as mpl
from scipy.optimize import minimize 

dx = 0.001 
x = np.arange(-10, 10, dx)

f = lambda x: x**2 * ( 1 - 0.1 * (x) **2 )* np.exp(- 0.1 * (x)**2) 
fig, ax = plt.subplots() 
ax.set(xlabel='x', ylabel='f(x)') 
ax.plot(x, f(x)) 
plt.show()

def get_path(xc): 
  global path 
  path.append(xc)
  
x0 = 2.4 
path = [x0] 
result = minimize(f, x0=x0, tol=1e-2, callback=get_path) 
x1 = result.x 
print(result)

plt.scatter([x0], [f(x0)], color = 'tab:green') 
plt.plot(path, [f(i) for i in path], '--o', color="black", lw=0.75, markersize=2) 
plt.scatter([x1], [f(x1)], color = 'tab:red') 
plt.plot(x, f(x), zorder = 0) 
plt.xlim(0, 10) 
plt.ylim(-3.5, 2) 
plt.show()

result = minimize(f, x0=1.5) 
x2 = result.x 
print(result)

plt.annotate("", xytext=(2.4, f(2.4)), xy=(x1, f(x1)), arrowprops=dict(arrowstyle="->")) 
plt.annotate("", xytext=(1.5, f(1.5)), xy=(x2, f(x2)), arrowprops=dict(arrowstyle="->")) 
plt.scatter([x1, x2], [f(x1), f(x2)], color = 'tab:red') 
plt.scatter([2.4, 1.5], [f(2.4), f(1.5)], color = 'tab:green') 
plt.plot(x, f(x), zorder=0) 
plt.show()

from scipy.optimize import differential_evolution 
result = differential_evolution(f, [(x.min(),x.max())]) 
print(result)
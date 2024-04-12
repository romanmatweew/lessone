import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib as mpl

import warnings 
mpl.style.use('seaborn-white') 
warnings.filterwarnings('ignore') 
dx = 0.001 
x = np.arange(-10, 10, dx) 
f0 = lambda x: (x - 0.5)**2 
plt.plot(x, f0(x)) 
plt.show()

from scipy.optimize import minimize 
result = minimize(f0, x0=1)
print(result.x[0])
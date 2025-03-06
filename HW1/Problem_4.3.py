import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)

y1 = np.sin(x)          
y2 = np.cos(x)          
y3 = np.exp(-0.3 * x)    

plt.plot(x, y1, 'r--', label='sin(x)')   
plt.plot(x, y2, 'g-.', label='cos(x)')   
plt.plot(x, y3, 'b-', label='exp(-0.3x)')  

plt.title('Multiple Curves in One Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.legend()

plt.show()

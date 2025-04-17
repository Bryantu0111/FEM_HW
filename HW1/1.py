import numpy as np
import matplotlib.pyplot as plt

def plot_equations(equations, x_range=(0,50), xlabel='X-axis', ylabel='Y-axis', y_value=1.0):
    x = np.linspace(x_range[0], x_range[1], 400)
    plt.figure(figsize=(8, 6))
    
    for eq in equations:
        y = eval(eq, {'x': x, 'np': np})  # 安全地評估方程
        plt.plot(x, y, label=f'$y = {eq}$')
    
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.axhline(y=y_value, color='red', linestyle='--', linewidth=1, label=f'Horizontal Line at y={y_value}')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

# 使用者輸入方程式
equations = ["-1.1+0.62*7+1.3*0.001*x+1.62*log(x)"]
plot_equations(equations, xlabel='Time (s)', ylabel='Value', y_value=1.0)
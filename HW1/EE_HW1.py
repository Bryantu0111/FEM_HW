import numpy as np
import matplotlib.pyplot as plt

def plot_equation(equation,equation_name, x_range=(1, 50), xlabel='X-axis', ylabel='Y-axis', y_values=(1.0, -1.0)):
    x = np.linspace(x_range[0], x_range[1], 400)
    plt.figure(figsize=(8, 6))
    
    y = eval(equation, {'x': x, 'np': np})  # 安全地評估方程
    plt.plot(x, y, label=f'{equation_name}')
    
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    
    # 繪製兩條水平線
    plt.axhline(y=y_values[0], color='red', linestyle='-', linewidth=1, label=f'ML_value{y_values[0]}')
    plt.axhline(y=y_values[1], color='blue', linestyle='-', linewidth=1, label=f'mb_value{y_values[1]}')
    
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

# 使用者輸入方程式
equation = "-1.1+0.62*7+1.3*0.001*x+1.62*np.log10(x)"
equation_name = "MS_value"
plot_equation(equation, equation_name, xlabel='r7 (km)', ylabel='Magnitude', y_values=(5.69, 5.09))
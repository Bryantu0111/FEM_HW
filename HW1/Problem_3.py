import numpy as np

def riemann_sum(f, a, b, n):
    dx = (b - a) / n  # 每個子區間的寬度
    x = np.linspace(a, b - dx, n)  # 左端點取樣
    return np.sum(f(x) * dx)  # 累加區間面積

# 定義要積分的函數
def f(x):
    return x**2*(x**3+1)**0.5

# 設定積分範圍
a, b = 0, 3

# 設定不同的 n 值進行計算
n_values = [5, 30, 100, 1000, 10000]

# 計算並輸出結果
for n in n_values:
    result = riemann_sum(f, a, b, n)
    print(f"n={n}, Riemann Sum={result}")
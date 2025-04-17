import numpy as np
import matplotlib.pyplot as plt

# 基本參數
q0 = 1
EI = 1
L = 1
pi = np.pi

# 定義 x 軸
x = np.linspace(0, L, 200)

# --------- Rayleigh-Ritz 係數 ---------

# N=1
C1_n1 = (-L**2 * q0 * (4 + pi**2)) / (4 * pi**3)
w_n1 = C1_n1 * x**2

# N=2
C1_n2 = (L**2 * q0 * (-6 * pi**2 - 8 * pi + 24 + pi**3)) / (2 * pi**4)
C2_n2 = (L * q0 * (-pi**3 - 16 + 4 * pi + 4 * pi**2)) / (2 * pi**4)
w_n2 = C1_n2 * x**2 + C2_n2 * x**3

# N=3
C1_n3 = (-L**2 * q0 * (72 * pi**3 + 600 - 7 * pi**4 - 84 * pi**2 - 288 * pi)) / (4 * pi**5)
C2_n3 = (L * q0 * (-48 * pi**2 - 128 * pi - 3 * pi**4 + 300 + 32 * pi**3)) / pi**5
C3_n3 = (5 * q0 * (-12 * pi**3 - 120 + pi**4 + 48 * pi + 20 * pi**2)) / (4 * pi**5)
w_n3 = C1_n3 * x**2 + C2_n3 * x**3 + C3_n3 * x**4

# 理論解（取負號）
w_exact = -(q0 / EI) * ((L / pi**4) * np.sin(pi * x / L)
                        - (1 / 6) * (L / pi) * x**3
                        + (1 / 2) * (L**2 / pi - L**2 / pi**4) * x**2
                        - (L / pi)**3 * x)

# --------- 數值導數 ---------
def derivative(y, x, n=1):
    for _ in range(n):
        y = np.gradient(y, x, edge_order=2)
    return y

# 各階導數
def get_all(w):
    theta = derivative(w, x, 1)
    moment = -EI * derivative(w, x, 2)
    shear = -EI * derivative(w, x, 3)
    return theta, moment, shear

# 取得 N=1,2,3 與 exact 的 θ, M, V
theta_n1, moment_n1, shear_n1 = get_all(w_n1)
theta_n2, moment_n2, shear_n2 = get_all(w_n2)
theta_n3, moment_n3, shear_n3 = get_all(w_n3)
theta_exact, moment_exact, shear_exact = get_all(w_exact)

# --------- 繪圖函數 ---------
def plot_comparison(y1, y2, y3, y_exact, ylabel, title):
    plt.figure(figsize=(8, 4))
    plt.plot(x, y_exact, label="Exact", color='black', linewidth=2)
    plt.plot(x, y1, ':', label="Rayleigh-Ritz N=1", linewidth=2)
    plt.plot(x, y2, '-.', label="Rayleigh-Ritz N=2", linewidth=2)
    plt.plot(x, y3, '--', label="Rayleigh-Ritz N=3", linewidth=2)
    plt.xlabel("x")
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# --------- 繪製四張圖 ---------
plot_comparison(w_n1, w_n2, w_n3, w_exact, "w(x)", "Displacement Comparison")
plot_comparison(theta_n1, theta_n2, theta_n3, theta_exact, "θ(x)", "Rotation Angle Comparison")
plot_comparison(moment_n1, moment_n2, moment_n3, moment_exact, "M(x)", "Bending Moment Comparison")
plot_comparison(shear_n1, shear_n2, shear_n3, shear_exact, "V(x)", "Shear Force Comparison")

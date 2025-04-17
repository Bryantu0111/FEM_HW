import numpy as np
import matplotlib.pyplot as plt

# 基本參數
q0 = 1
EI = 1
L = 1
pi = np.pi

# 定義 x 範圍
x = np.linspace(0, L, 200)

# 理論解（取負號）
w_exact = -(q0 / EI) * ((L / pi**4) * np.sin(pi * x / L)
                        - (1 / 6) * (L / pi) * x**3
                        + (1 / 2) * (L**2 / pi - L**2 / pi**4) * x**2
                        - (L / pi)**3 * x)

# --------- Rayleigh-Ritz N = 1 ---------
C1_n1 = (-L**2 * q0 * (4 + pi**2)) / (4 * pi**3)
w_approx_n1 = C1_n1 * x**2

# --------- Rayleigh-Ritz N = 2 ---------
C1_n2 = (L**2 * q0 * (-6 * pi**2 - 8 * pi + 24 + pi**3)) / (2 * pi**4)
C2_n2 = (L * q0 * (-pi**3 - 16 + 4 * pi + 4 * pi**2)) / (2 * pi**4)
w_approx_n2 = C1_n2 * x**2 + C2_n2 * x**3

# --------- Rayleigh-Ritz N = 3 ---------
C1_n3 = (-L**2 * q0 * (72 * pi**3 + 600 - 7 * pi**4 - 84 * pi**2 - 288 * pi)) / (4 * pi**5)
C2_n3 = (L * q0 * (-48 * pi**2 - 128 * pi - 3 * pi**4 + 300 + 32 * pi**3)) / pi**5
C3_n3 = (5 * q0 * (-12 * pi**3 - 120 + pi**4 + 48 * pi + 20 * pi**2)) / (4 * pi**5)
w_approx_n3 = C1_n3 * x**2 + C2_n3 * x**3 + C3_n3 * x**4

# --------- 繪圖 ---------
plt.figure(figsize=(8, 5))
plt.plot(x, w_exact, label="Exact Solution", linewidth=2)
plt.plot(x, w_approx_n1, ':', label="Rayleigh-Ritz N=1", linewidth=2)
plt.plot(x, w_approx_n2, '-.', label="Rayleigh-Ritz N=2", linewidth=2)
plt.plot(x, w_approx_n3, '--', label="Rayleigh-Ritz N=3", linewidth=2)
plt.xlabel("x")
plt.ylabel("w(x)")
plt.title("Comparison of Exact and Rayleigh-Ritz Approximate Solutions (N=1,2,3)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

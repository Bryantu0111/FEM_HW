# 對 w_exact、w1、w2、w3 分別取一階、二階、三階導數以求：旋轉角（w'）、彎矩（M=-EI w''）、剪力（V=-EI w'''）

# 將符號解轉為 SymPy 表達式（重新定義 EI=1, q0=1, L=1）
EI_val = 1

# 理論解 w_exact 轉換成 sympy 表達式
w_exact_expr = - ((x / pi**4) * sp.sin(pi * x) -
                  (1 / 6) * (1 / pi) * x**3 +
                  (1 / 2) * (1 / pi - 1 / pi**4) * x**2 -
                  (1 / pi)**3 * x)

# 求各解的一階、二階、三階導數
def get_derivatives(w_expr):
    w1 = sp.diff(w_expr, x, 1)
    M = -EI_val * sp.diff(w_expr, x, 2)
    V = -EI_val * sp.diff(w_expr, x, 3)
    return w1, M, V

# 計算所有解的導數
w1p, M1, V1 = get_derivatives(C1 * x**2)
w2p, M2, V2 = get_derivatives(w2_expr)
w3p, M3, V3 = get_derivatives(w3_expr)
w_exact_p, M_exact, V_exact = get_derivatives(w_exact_expr)

# 轉為可數值化的 numpy 函數
def lambdify_all(exprs):
    return [sp.lambdify(x, expr, 'numpy') for expr in exprs]

w_funcs = lambdify_all([w1p, w2p, w3p, w_exact_p])
M_funcs = lambdify_all([M1, M2, M3, M_exact])
V_funcs = lambdify_all([V1, V2, V3, V_exact])

# 計算數值結果
w_rot_vals = [f(x_vals) for f in w_funcs]
M_vals = [f(x_vals) for f in M_funcs]
V_vals = [f(x_vals) for f in V_funcs]

# 繪製三張圖：旋轉角、彎矩、剪力
titles = ["Slope (w')", "Bending Moment (M = -EI w'')", "Shear Force (V = -EI w''')"]
ylabels = ["w'(x)", "M(x)", "V(x)"]
all_vals = [w_rot_vals, M_vals, V_vals]
labels = [r'$w_1$', r'$w_2$', r'$w_3$', r'$w_{exact}$']
styles = ['--', '-.', ':', '-']

for i in range(3):
    plt.figure(figsize=(8, 5))
    for val, label, style in zip(all_vals[i], labels, styles):
        plt.plot(x_vals, val, style, label=label, linewidth=2)
    plt.title(titles[i])
    plt.xlabel("x")
    plt.ylabel(ylabels[i])
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    # 將 w1 的導數部分明確代入 C1 的數值（避免符號未定義錯誤）
C1_val = -0.0322515344331995
w1_expr_fixed = C1_val * x**2
w1p_fixed, M1_fixed, V1_fixed = get_derivatives(w1_expr_fixed)

# 更新 w_funcs, M_funcs, V_funcs
w_funcs = lambdify_all([w1p_fixed, w2p, w3p, w_exact_p])
M_funcs = lambdify_all([M1_fixed, M2, M3, M_exact])
V_funcs = lambdify_all([V1_fixed, V2, V3, V_exact])

# 數值化
w_rot_vals = [f(x_vals) for f in w_funcs]
M_vals = [f(x_vals) for f in M_funcs]
V_vals = [f(x_vals) for f in V_funcs]

# 繪製三張圖：旋轉角、彎矩、剪力
titles = ["Slope (w')", "Bending Moment (M = -EI w'')", "Shear Force (V = -EI w''')"]
ylabels = ["w'(x)", "M(x)", "V(x)"]
all_vals = [w_rot_vals, M_vals, V_vals]
labels = [r'$w_1$', r'$w_2$', r'$w_3$', r'$w_{exact}$']
styles = ['--', '-.', ':', '-']

for i in range(3):
    plt.figure(figsize=(8, 5))
    for val, label, style in zip(all_vals[i], labels, styles):
        plt.plot(x_vals, val, style, label=label, linewidth=2)
    plt.title(titles[i])
    plt.xlabel("x")
    plt.ylabel(ylabels[i])
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    # 確保所有結果都是與 x_vals 對應的向量（300點）
def ensure_vector_output(f):
    result = f(x_vals)
    if np.isscalar(result):
        return np.full_like(x_vals, result)
    return result

# 確保每一個函數輸出為 vector
w_rot_vals = [ensure_vector_output(f) for f in w_funcs]
M_vals = [ensure_vector_output(f) for f in M_funcs]
V_vals = [ensure_vector_output(f) for f in V_funcs]

# 再次繪圖
titles = ["Slope (w')", "Bending Moment (M = -EI w'')", "Shear Force (V = -EI w''')"]
ylabels = ["w'(x)", "M(x)", "V(x)"]
all_vals = [w_rot_vals, M_vals, V_vals]
labels = [r'$w_1$', r'$w_2$', r'$w_3$', r'$w_{exact}$']
styles = ['--', '-.', ':', '-']

for i in range(3):
    plt.figure(figsize=(8, 5))
    for val, label, style in zip(all_vals[i], labels, styles):
        plt.plot(x_vals, val, style, label=label, linewidth=2)
    plt.title(titles[i])
    plt.xlabel("x")
    plt.ylabel(ylabels[i])
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
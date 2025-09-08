import numpy as np

def get_coordinates():
    print("請輸入三個節點的座標（格式：x y）：")
    x1, y1 = map(float, input("節點1: ").split())
    x2, y2 = map(float, input("節點2: ").split())
    x3, y3 = map(float, input("節點3: ").split())
    return (x1, y1), (x2, y2), (x3, y3)

def calculate_Ae(x1, y1, x2, y2, x3, y3):
    return 0.5 * abs(
        x1 * (y2 - y3) +
        x2 * (y3 - y1) +
        x3 * (y1 - y2)
    )

def calculate_beta_gamma(x1, y1, x2, y2, x3, y3):
    beta = [y2 - y3, y3 - y1, y1 - y2]
    gamma = [x3 - x2, x1 - x3, x2 - x1]
    return beta, gamma

def calculate_K_matrix(Ae, beta, gamma):
    K = np.zeros((3, 3))
    for i in range(3):
        for j in range(3):
            K[i, j] = (1 / (4 * Ae)) * (beta[i] * beta[j] + gamma[i] * gamma[j])
    return K

def main():
    (x1, y1), (x2, y2), (x3, y3) = get_coordinates()
    Ae = calculate_Ae(x1, y1, x2, y2, x3, y3)
    beta, gamma = calculate_beta_gamma(x1, y1, x2, y2, x3, y3)
    K = calculate_K_matrix(Ae, beta, gamma)

    print(f"\n三角形元素面積 Ae = {Ae:.4f}\n")

    print("β值:")
    for i, b in enumerate(beta, start=1):
        print(f"β{i} = {b:.4f}")

    print("\nγ值:")
    for i, g in enumerate(gamma, start=1):
        print(f"γ{i} = {g:.4f}")

    print("\nK 矩陣（3x3）:")
    for i in range(3):
        for j in range(3):
            print(f"K{i+1}{j+1} = {K[i, j]:.4f}", end='\t')
        print()

if __name__ == "__main__":
    main()

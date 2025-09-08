import numpy as np

def main():
    print("5x5 聯立方程組解算器")

    # Step 1: 輸入變數名稱
    vars_input = input("請輸入五個變數名稱（例如：x1 x2 x3 x4 x5）：").strip().split()
    if len(vars_input) != 5:
        print("❌ 必須輸入五個變數名稱！")
        return

    # Step 2: 輸入 5x5 係數矩陣
    print("請依序輸入 5x5 的係數矩陣，每列用空格分隔")
    coeff_matrix = []
    for i in range(5):
        row = list(map(float, input(f"第 {i+1} 列：").strip().split()))
        if len(row) != 5:
            print("❌ 每列必須包含 5 個數字")
            return
        coeff_matrix.append(row)

    A = np.array(coeff_matrix)

    # Step 3: 輸入右側常數項
    b_input = input("請輸入等號右邊的五個常數（用空格分隔）：")
    b = np.array(list(map(float, b_input.strip().split())))

    if len(b) != 5:
        print("❌ 常數項數量應為 5")
        return

    # Step 4: 解聯立方程組
    try:
        x = np.linalg.solve(A, b)
        print("\n✅ 解如下：")
        for var, val in zip(vars_input, x):
            print(f"{var} = {val:.4f}")
    except np.linalg.LinAlgError as e:
        print(f"\n❌ 無法解這個方程組：{e}")

if __name__ == "__main__":
    main()

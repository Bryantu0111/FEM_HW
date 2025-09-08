def main():
    print("請輸入 x 與 y 的值（空格分隔，例如：0.5 0.3）:")
    x, y = map(float, input("輸入: ").split())

    result = (5 / 2) * (1 - x**2 - y**2)

    print(f"\n計算結果為: {result:.4f}")

if __name__ == "__main__":
    main()

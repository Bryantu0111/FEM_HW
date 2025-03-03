def power_of_x(m, x):
    sum = 0
    for m in range(m+1):
        sum += (x**m)
    return sum
# 測試程式碼
x = float(input("請輸入一個公比 x: "))

m_lst = 1/(1-x)

m_values = [3, 10, 50, 200, 400]

for m in m_values:
    print(f"公比是{x}時，總和是: {power_of_x(m, x)}")

print(f'm是1/(1-x)時,總和是{power_of_x(m_lst, x)}')
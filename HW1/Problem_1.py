def product_of_m(m):
    if m % 2 == 0:
        raise ValueError("m 必須是奇數")
    
    result_1 = 1
    result_2 = 1
    result_3 = 1
    for i in range(1, m + 1):
        result_1 *= i
        result_2 += i
        result_3 += 1 / i
    
    return result_1, result_2, result_3

# 測試程式碼
m = int(input("請輸入一個奇數 m: "))
print(f"{m} 連續相乘的結果是: {product_of_m(m)}")

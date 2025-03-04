def series(x,m):
    if x == 1:
        return m
    else:
        return (1-x**m)/(1-x) 
x = float(input('請輸入一個公比:'))
m_table = [3, 10, 50, 200, 400]

m_lst = [1/(1-x)]
for m in m_table + m_lst:
    print(f'公比是{x}時，總和是{series(x,m)} ')
orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'
orders = list(orders.split(","))

ice = list(filter(lambda x:  x[:3] == '아이스', orders))
print(len(ice))

dic1 = {}
for coffee in orders:
    if coffee in dic1:
        dic1[coffee] += 1 
    else:
        dic1[coffee] = 1

for k, v in dic1.items():
    print(k, v)
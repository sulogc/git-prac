n = int(input())

if n < 100:
    print(n)

else:
    cnt = 99
    for i in range(100, n+1):
        
        dis = int(str(i)[0]) - int(str(i)[1])
        k = 1 
        for j in range(1, len(str(i))-1):
            if dis != int(str(i)[j]) - int(str(i)[j+1]):
                k = 0
        cnt += k
    print(cnt)    
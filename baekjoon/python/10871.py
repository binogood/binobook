a, b = map(int, input().split())
num = list(map(int,input().split()))
for i in range(a):
    if b > num[i]:
        print(num[i], end=" ")

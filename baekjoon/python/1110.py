a = int(input())
num = a
cnt = 0
tmp = 0
tmp2 = 0
while True:
    tmp = a//10 + a%10
    tmp2 = (a%10)*10 + tmp%10
    cnt += 1
    a = tmp2
    if a == num:
        break
print(cnt)

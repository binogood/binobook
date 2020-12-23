n = int(input())
sub = list(map(int, input().split()))
m_max = max(sub)
for i in range(n):
    sub[i] = sub[i]/m_max*100
avg = sum(sub) / n
print("%.2f" %avg)

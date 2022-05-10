a = list(map(int, input().split()))
n, k = map(int, input().split())
print(sum(a[n: k + 1]))

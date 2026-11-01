n = int(input("Enter number of items: "))

w = []
p = []

for i in range(n):
    w.append(int(input("Enter weight: ")))
    p.append(int(input("Enter profit: ")))

W = int(input("Enter bag capacity: "))

dp = [0] * (W + 1)

for i in range(n):
    for j in range(W, w[i]-1, -1):
        dp[j] = max(dp[j], p[i] + dp[j-w[i]])

print("Maximum Profit:", dp[W])
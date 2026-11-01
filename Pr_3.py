n = int(input("Enter number of items: "))

items = []

for i in range(n):
    w = int(input("Enter weight: "))
    p = int(input("Enter profit: "))
    items.append((p/w, w, p))

capacity = int(input("Enter bag capacity: "))

items.sort(reverse=True)

total = 0

for r, w, p in items:
    if capacity >= w:
        total += p
        capacity -= w
    else:
        total += r * capacity
        break

print("Maximum Profit:", total)
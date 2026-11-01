steps = 0

def fib(n):
    global steps
    steps += 1
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

n = int(input("Enter Terms: "))

print("Recursive: ")
for i in range(n):
    print(fib(i), end=" ")
    
print("\nRecursive Steps: ", steps)

a, b = 0, 1
steps = 0

print("Non Recursive: ")
for i in range(n):
    print(a, end=" ")
    a, b = b, a+b
    steps += 1
    
print("\nNon Recursive Steps: ", steps)
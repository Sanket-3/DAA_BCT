import heapq

n = int(input("Enter number of characters: "))
heap = []

for i in range(n):
    ch = input("Enter character: ")
    f = int(input("Enter frequency: "))
    heap.append((f, ch))

heapq.heapify(heap)

while len(heap) > 1:
    f1, a = heapq.heappop(heap)
    f2, b = heapq.heappop(heap)
    heapq.heappush(heap, (f1+f2, (a, b)))

def display(tree, code=""):
    if isinstance(tree, str):
        print(tree, ":", code)
    else:
        display(tree[0], code+"0")
        display(tree[1], code+"1")

print("Huffman Codes:")
display(heap[0][1])
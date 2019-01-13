n=32
k=5  #n and k taken from the dataset
def fibonacciRab(n, k):
    a, b = 1, 1
    for i in range(2, n):
        a, b = b, k*a + b
    return b
print(fibonacciRab(n,k))

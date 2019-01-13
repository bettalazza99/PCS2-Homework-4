n=97
m=17
def fibd(n,m):
    ages = [1] + [0]*(m-1)
    for i in range(n-1):
        ages = [sum(ages[1:])] + ages[:-1]
    return sum(ages)
print (fibd(n,m))

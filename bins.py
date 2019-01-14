def Bin_Search(array, val):
	return Bin_Search_Help(array, val, 0, len(array))
def Bin_Search_Help(array, val, x, y):
	if x >= y:
		return -1
	elif x == y-1:
		if array[x] == val:
			return x+1
		else:
			return -1
	midpoint = (x + y) // 2
	if array[midpoint] > val:
		return Bin_Search_Help(array, val, x, midpoint)
	else:
		return Bin_Search_Help(array, val, midpoint, y)

if __name__ == '__main__':
    f= open('C:\\Users\\Elisabetta\\Desktop\\rosalind_bins.txt')
    n = int(f.readline())
    m = int(f.readline())
    array = list(map(int, f.readline().split()))
    ks = list(map(int, f.readline().split()))

print(' '.join(map(str, [Bin_Search(array, val) for val in ks])))

n = int(input().strip())

a = list(map(int, input().rstrip().split()))

l = len(a)

def swap(a):
    cmpcount, swapcount = 0, 0
    for i in range(0,l):
        for j in range(0,l-1):
            cmpcount += 1
            if a[j]>a[j+1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapcount += 1
    print(f"Array is sorted in {swapcount} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")

swap(a)
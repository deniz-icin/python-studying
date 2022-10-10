

if __name__ == '__main__':
    n = int(input().strip())
    
    a = bin(n)
    
    consecutive = a.split('0')
    
    print(max(consecutive, key = len))

n = int(input())

for i in range(0, n):
    s = input()
    evenStr = ""
    oddStr = ""
    
    for i in range(0, len(s)):
        if i % 2 == 0:
            evenStr += s[i]
        else:
            oddStr += s[i]
            
    print(evenStr,oddStr)
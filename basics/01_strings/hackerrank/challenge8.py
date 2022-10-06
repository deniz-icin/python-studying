
n = int(input())
phone_book = {}

for _ in range(n):
    name,phone=input().split()
    phone_book[name] = [phone]
    d = phone_book
    
for _ in d:
    query = input()
    if _ != query:
        print("Not found")
    else:
        print(name + "=" + phone)
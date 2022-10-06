

n = int(input())
phone_book = {}

for _ in range(n):
    name,phone=input().split()
    phone_book[name] = [phone]

d = phone_book    

for _ in range(len(d)):
    query = input()
    if query not in phone_book:
        print("Not found")
    else:
        print(query + "=" + [phone])
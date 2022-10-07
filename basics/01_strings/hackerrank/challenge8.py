

n = int(input())
phone_book = {}

for _ in range(n):
    name,phone=input().split()
    phone_book[name] = [phone]

d = phone_book    


def main():
    query = input()
    if query not in d:
        print("Not found")
    else:
        output = f'{query} = {phone_book[query]}'
        print(output)



for _ in range(n):
   main()

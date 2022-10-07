

n = int(input())
phone_book = {}

for _ in range(n):
    name, phone_number = str(input()).split(" ")
    phone_book[name] = phone_number
    
def main():
    query = input()
    if query not in phone_book:
        print("Not found")
    else:
        output = f'{query}={phone_book[query]}'
        print(output)


for _ in range(n):
   main()

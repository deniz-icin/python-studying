

n = int(input())
phone_book = {}

for _ in range(n):
    name, phone_number = str(input()).split(" ")
    phone_book[name] = phone_number
    
while True:
    try:
        query = str(input())
        print(f"{query}={phone_book[query]}")
    except KeyError:
        print("Not found")
    except EOFError:
        break


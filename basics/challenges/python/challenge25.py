def is_prime():
    n = int(input())
    prime_range = range(2, int(n**0.5) + 1)
    conditions = sum((n % i) == 0 for i in prime_range) == 0 and n != 1
    print("Prime") if conditions else print("Not prime")


T = int(input())
for _ in range(T):
    is_prime()
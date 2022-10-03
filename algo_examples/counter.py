
from pprint import pprint

siklik = {}
girdi = input("bir metin giriniz:")

for character in sorted(girdi):
    if character in siklik.keys():
        siklik[character] += 1
    else:
        siklik[character] = 1

pprint(siklik)
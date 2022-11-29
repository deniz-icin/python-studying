data = {
    "100-90": 25, "42-01": 48, "55-09": 12, "128-64": 71, "002-22": 18, "321-54": 19, "097-32": 33, "065-135": 64, "99-043": 80, "111-99": 11, "123-019": 5, "109-890": 72, "132-123": 27, "32-908": 27, "008-09": 25, "055-967": 35, "897-99": 44, "890-98": 56, "344-32": 65, "43-955": 59, "001-233": 9, "089-111": 15, "090-090": 17, "56-777": 23, "44-909": 27, "13-111": 21, "87-432": 15, "87-433": 14, "87-434": 23, "87-435": 11, "87-436": 12, "87-437": 16, "94-121": 15, "94-122": 35, "80-089": 10, "87-456": 8, "87-430": 40
}
discount_age = int(input())
adults = 0
children = 0

for i in data.values():
    if i < 18: # discount age taken 18 while calculating money_on_hand
        children += 1
    else:
        adults += 1

money_on_hand = children*5 + adults*20

new_adults = 0
new_children = 0

for i in data.values():
    if i < discount_age: # if we change the discount_age 18 to whatever we want:
        new_children += 1
    else:
        new_adults += 1

max_money = new_children*5 + new_adults*20

print(int((max_money-money_on_hand)/money_on_hand*100))

age = int(input().strip())
day = int(input().strip())

if age < 13:
    price = 100
elif age <= 60:
    price = 180
else:
    price = 120

if day in (6, 7):
    price += 50

print(price)

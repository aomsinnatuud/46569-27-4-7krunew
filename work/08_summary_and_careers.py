a = float(input("ป้อนยอดบิล: "))
b = float(input("เปอร์เซ็นต์ทิป: "))
c = int(input("จำนวนคน: "))

tip = a * (b / 100)
total = a + tip
each = total / c

print(f"Each person pays: {each:.2f}")
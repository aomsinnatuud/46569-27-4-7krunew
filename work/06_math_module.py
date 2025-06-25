import math

x1, y1, x2, y2 = map(float, input("ป้อนค่าพิกัด x1 y1 x2 y2: ").split())
cc = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"{cc:.1f}")

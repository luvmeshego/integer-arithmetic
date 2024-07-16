x1 = int(input())
y1 = int(input())
a1 = int(input())
b1 = int(input())
x2 = int(input())
y2 = int(input())
n = (x2 - x1) * 60 + (y2 - y1)
time = a1 * 60 + b1 + n * 2
hours = (time // 60) % 24
minutes = time % 60
print(hours, minutes)
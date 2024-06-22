a = int(input())
b = int(input())
L = int(input())
N = int(input())
free = 2 * L
vertical = b * (N - 1) * 2
horizontal = a * (N - 1) * 2 + a
print(free + vertical + horizontal)
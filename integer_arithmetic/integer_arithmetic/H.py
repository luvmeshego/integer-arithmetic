a = int(input())
b = int(input())
n = int(input())
rubl = a * n
kop = (b * n) % 100
kop_ost = (b * n) // 100
print(rubl + kop_ost, kop)
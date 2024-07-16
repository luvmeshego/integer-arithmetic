n = int(input())
sec = (n % 60)
minute = (n // 60) % 60
hour = (n // 3600) % 24
ost_sec = (sec % 100) // 10
ost_min = (minute % 100) // 10
print(str(hour) + ':' + str(ost_min) + str(minute % 10) + ':' + str(ost_sec) + str(sec % 10))
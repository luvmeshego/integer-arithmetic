n = int(input())
sec = n % 60
minute = n  % 60
hour = (n // 3600) % 24
print('0' hour,':', minute,':', sec)
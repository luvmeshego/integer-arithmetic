a = int(input())
time_lesson = a * 45
fifteen = (a - 1) // 2 * 15
five = ((a - 1) % 2 + (a - 1)) // 2 * 5
hours = (9 + (time_lesson + five + fifteen) // 60) % 24
minutes = (time_lesson + five + fifteen) % 60
print(hours, minutes)
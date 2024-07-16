first = int(input())
second = int(input())
third = int(input())
rest_first = first % 2
rest_second = second % 2
rest_third = third % 2
desk_first = (rest_first + first) // 2
desk_second = (rest_second + second) // 2
desk_third = (rest_third + third) // 2
print(desk_first + desk_second + desk_third)
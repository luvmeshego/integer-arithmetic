N = int(input())
M = int(input())
maximum = ((N - M) / 2) * (N - M + 1)
teams_with_more_people = N % M
teams_with_less_people = M - teams_with_more_people
less_quantity = N // M
more_quantity = less_quantity + 1
less_team_handshakes = (less_quantity - 1) / 2 * less_quantity
more_team_handshakes = (more_quantity - 1) / 2 * more_quantity
minimum = (less_team_handshakes * teams_with_less_people) + (more_team_handshakes * teams_with_more_people)
print(int(minimum), int(maximum))

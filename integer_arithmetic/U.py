N = int(input())
M = int(input())
maximum = ((N - M) // 2) * (N - M + 1)
more = N % M
less = M - more
less_quantity = N // M
minimum = (N // M - 1) * less
print(minimum, maximum)
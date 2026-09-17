x, y = map(int, input().split())
print((x % y == 0) or (y % x == 0))
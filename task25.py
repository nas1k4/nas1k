a, b, c = map(int, input().split())

s = (a * 100 + b) * c
r = s // 100
k = s % 100

print(f"{r} руб. {k} коп.")
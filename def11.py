fruits = [list('apple'), list('banana'), list('cherry'), [], [], list('fig')]


def my_fruit(fruits):
    for i, ch in enumerate(fruits):
        print(f'{i}: {", ".join(ch)}')

my_fruit(fruits)

# 예상 출력
# 0: a, p, p, l, e
# 1: b, a, n, a, n, a
# 2: c, h, e, r, r, y
# 3:
# 4:
# 5: f, i, g

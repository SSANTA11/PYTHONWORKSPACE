# 1 회차
def my_print(fruits):
    for i in range(len(fruits)):
        for r in range(len(fruits[i])):
            print(fruits[i][r],end="")
        print()



fruits=[['A', 'p', 'p', 'l', 'e'],
        ['B', 'a', 'n', 'a', 'n', 'a'],
        ['C', 'h', 'e', 'r', 'r', 'y']]

my_print(fruits)

# 2회차 gpt 참고
def mp(fruits):
    for ch in fruits:
        print("".join(ch))

mp(fruits)
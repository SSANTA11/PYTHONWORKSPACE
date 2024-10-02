numbers=[273, 103, 5, 32, 65, 9, 72, 800, 99]
for number in numbers:
    if number>99:
        print(f"{number} 는 3 자릿수입니다.")
    elif number>9:
        print(f"{number} 는 2 자릿수입니다.")
    elif number>=1:
        print(f"{number} 는 1 자릿수입니다.")
    else:
        print("이 문장은 보여서는 안됩니다!")
a_diet={"morning":"reality", "evening":"life", "afternoon":"feeling"}
b_diet={"dawn":"grief"}
diet=[a_diet,b_diet]


for foods in diet:
    for food in foods:
        print(food)
        print(foods[food])
        print()
    print()
print("-=-"*20)


a_diet["morning"]="goal"
b_diet["dawn"]="beam"
b_diet["anytime"]="exciting"


for foods in diet:
    for food in foods:
        print(food)
        print(foods[food])
        print()
    print()
print("-=-"*20)
character={
    "name":"기사",
    "level":"12", 
    "items":{
        "sword":"불꽃의 검", 
        "armor":"풀플레이트"
            }, 
    "skill":["베기", "세게 베기", "아주 세게 베기"]
          }

for key in character:
    if type(character[key])==str:
        print(f"{key} : {character[key]}")

    elif type(character[key])==dict:
        for key_a in character[key]:
            print(f"{key_a} : {character[key][key_a]}")

    else :
        for list_a in character[key]:
            print(f"{key} : {list_a}")
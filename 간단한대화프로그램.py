a=input("말씀하시고픈 대화문을 입력해주세요!")

from datetime import datetime
from pytz import timezone
now=datetime.now(timezone('Asia/Seoul'))

if ("안녕" in a) or ("반가워" in a):
    print("안녕하세요!")

elif ("몇 시"in a) or ("몇시" in a):
    print(f"지금은 {now.hour}시 {now.minute}분 입니다!")

else :
    print("죄송합니다. 해당 문장에 대한 반응은 준비되지 않았습니다.")
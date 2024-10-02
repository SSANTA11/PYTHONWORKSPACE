import datetime
import pytz

seoul=pytz.timezone("Asia/Seoul")
now = datetime.datetime.now(seoul)

print(f"찾으시는 현재 시간은... \n{now.year}년 {now.month}월 {now.day}일 {now.hour}시 {now.minute}분 {now.second}초 이고")


if now.hour < 12:
    print("오전이며")
if now.hour >= 12:
    print("오후이며")


if now.month==12:
    print("겨울입니다!")
if now.month<=2:
    print("겨울입니다!")
if 3 <= now.month <= 5:
    print("봄입니다!")
if 6 <= now.month <= 8:
    print("여름입니다!")
if 9 <= now.month <= 11:
    print("가을입니다!")
print()
print("-=-=-"*10)
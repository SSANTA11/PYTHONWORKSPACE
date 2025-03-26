from datetime import datetime
from pytz import timezone

today=datetime.now(timezone('Asia/Seoul'))

if today.hour>=12:
    print("오후입니다!")
else:
    print("오전입니다!")
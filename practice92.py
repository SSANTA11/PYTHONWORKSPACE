import time
시작시간=time.time()
현재시간=time.time()

while 현재시간<시작시간+5:
    print(현재시간, 시작시간+5)
    현재시간=time.time()
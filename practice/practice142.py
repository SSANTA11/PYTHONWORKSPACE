week='월화수목금토일'
print("{0:<7}".format(week[6]),end="")
for i in range(6):
    print("{0:<7}".format(week[i]), end="")
print()

list_a=[]

for r in range(1,31+1):
    list_a.append("{0:>2}".format(r))


from random import randint
num=randint(0,6)

start_day=[1,8,15,22,29,36,43]
select=start_day[num]

if select==1:
    for n in range(7):
        print("{0:<8}".format(list_a[n]),end="")
    print()
    for n in range(7,14):    
        print("{0:<8}".format(list_a[n]),end="")
    print()
    for n in range(14,21):
        print("{0:<8}".format(list_a[n]),end="")
    print()
    for n in range(21,28):
        print("{0:<8}".format(list_a[n]),end="")
    print()
    for n in range(28,31):
        print("{0:<8}".format(list_a[n]),end="")
    print()

if select==8:
    print("        ",end="")
    for n in range(0,6):
        print("{0:<8}".format(list_a[n]),end="")
    print()
    for n in range(6,13):    
        print("{0:<8}".format(list_a[n]),end="")
    print()
    for n in range(13,20):
        print("{0:<8}".format(list_a[n]),end="")
    print()
    for n in range(20,27):
        print("{0:<8}".format(list_a[n]),end="")
    print()
    for n in range(27,31):
        print("{0:<8}".format(list_a[n]),end="")
    print()

if select==15:
    print("        "*2,end="")
    for n in range(0,5):
        print("{0:<8}".format(list_a[n]),end="")
    print()
    for n in range(5,12):    
        print("{0:<8}".format(list_a[n]),end="")
    print()
    for n in range(12,19):
        print("{0:<8}".format(list_a[n]),end="")
    print()
    for n in range(19,26):
        print("{0:<8}".format(list_a[n]),end="")
    print()
    for n in range(27,31):
        print("{0:<8}".format(list_a[n]),end="")
    print()

if select==22:
    print("        "*3,end="")
    for n in range(0,4):
        print("{0:<8}".format(list_a[n]),end="")
    print()
    for n in range(4,11):    
        print("{0:<8}".format(list_a[n]),end="")
    print()
    for n in range(11,18):
        print("{0:<8}".format(list_a[n]),end="")
    print()
    for n in range(18,25):
        print("{0:<8}".format(list_a[n]),end="")
    print()
    for n in range(25,31):
        print("{0:<8}".format(list_a[n]),end="")
    print()

if select==29:
    print("        "*4,end="")
    for n in range(0,3):
        print("{0:<8}".format(list_a[n]),end="")
    print()
    for n in range(3,10):    
        print("{0:<8}".format(list_a[n]),end="")
    print()
    for n in range(10,17):
        print("{0:<8}".format(list_a[n]),end="")
    print()
    for n in range(17,24):
        print("{0:<8}".format(list_a[n]),end="")
    print()
    for n in range(24,31):
        print("{0:<8}".format(list_a[n]),end="")
    print()
    
if select==36:
    print("        "*5,end="")
    for n in range(0,2):
        print("{0:<8}".format(list_a[n]),end="")
    print()
    for n in range(2,9):    
        print("{0:<8}".format(list_a[n]),end="")
    print()
    for n in range(9,16):
        print("{0:<8}".format(list_a[n]),end="")
    print()
    for n in range(16,23):
        print("{0:<8}".format(list_a[n]),end="")
    print()
    for n in range(23,30):
        print("{0:<8}".format(list_a[n]),end="")
    print()
    for n in range(30,31):
        print("{0:<8}".format(list_a[n]),end="")
    print()
    
if select==43:
    print("        "*6,end="")
    for n in range(0,1):
        print("{0:<8}".format(list_a[n]),end="")
    print()
    for n in range(1,8):    
        print("{0:<8}".format(list_a[n]),end="")
    print()
    for n in range(8,15):
        print("{0:<8}".format(list_a[n]),end="")
    print()
    for n in range(15,22):
        print("{0:<8}".format(list_a[n]),end="")
    print()
    for n in range(22,29):
        print("{0:<8}".format(list_a[n]),end="")
    print()
    for n in range(29,31):
        print("{0:<8}".format(list_a[n]),end="")
    print()
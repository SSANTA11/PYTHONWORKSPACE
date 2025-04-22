# def factorial(n):
#     result=1
#     for i in range(1,n+1):
#         result=result*i
#     return result

# def fac(n):
#     if(n==1):
#         return 1
#     else:
#         return n*fac(n-1)
# print(fac(5))

# class Time:
#     def __init__(self,h,m,s):
#         self.h=h
#         self.m=m
#         self.s=s
#     def set(self,h,m,s):
#         self.h=h
#         self.m=m
#         self.s=s
#         return self.h, self.m, self.s
#     def hour(self):
#         return self.h
#     def minutes(self):
#         return self.m
#     def second(self):
#         return self.s
#     def isAM(self):
#         return self.hour<12
#     def isSame(self, t2):
#         return t2.h==self.h and t2.m==self.m and t2.s==self.s
#     def difference(self, t2):
#         t3=Time(self.h-t2.h,self.m-t2.m,self.s-t2.s)
#         return t3
#     def display(self):
#         print(f"현재 시각은 {self.hour()}시 {self.minutes()}분 {self.seconds}초입니다.")


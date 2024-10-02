
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 데이터
land_sizes = np.array([50, 70, 90, 110, 130]).reshape(-1, 1)  # 지대 크기
prices = np.array([100, 150, 200, 250, 300])  # 지가
residents = np.array([3, 4, 5, 6, 7])  # 거주자 수

# 산점도 시각화
plt.scatter(land_sizes, residents, color='blue', label='데이터 포인트')
plt.xlabel('지대 크기 (평방미터)')
plt.ylabel('거주자 수')
plt.title('지대 크기와 거주자 수의 관계')
plt.legend()
plt.show()

# 선형 회귀 모델 피팅
model = LinearRegression()
model.fit(land_sizes, residents)

# 회귀선 시각화
plt.scatter(land_sizes, residents, color='blue', label='데이터 포인트')
plt.plot(land_sizes, model.predict(land_sizes), color='red', label='회귀선')
plt.xlabel('지대 크기 (평방미터)')
plt.ylabel('거주자 수')
plt.title('선형 회귀분석 결과')
plt.legend()
plt.show()

# 회귀계수 출력
print("절편 (intercept):", model.intercept_)
print("기울기 (slope):", model.coef_)
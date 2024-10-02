import matplotlib.pyplot as plt
import numpy as np

# 가상의 주택 데이터 생성
np.random.seed(42)
house_size = np.random.normal(1500, 300, 100)
house_age = np.random.normal(10, 5, 100)
house_price = 50000 + 300 * house_size - 200 * house_age + np.random.normal(0, 5000, 100)

# 산점도 그리기
plt.scatter(house_size, house_price, label='House Price')
plt.xlabel('House Size (sqft)')
plt.ylabel('House Price ($)')
plt.legend()
plt.title('Scatter Plot of House Size vs. House Price')
plt.show()

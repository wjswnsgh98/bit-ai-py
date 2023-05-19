import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
#from sklearn.datasets import load_boston #윤리적 문제로 제공안됨
from sklearn.datasets import fetch_california_housing
import time

#1. 데이터
#datasets = load_boston()
datasets = fetch_california_housing()
x = datasets.data
y = datasets.target

print(datasets.feature_names)
# ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']
print(datasets.DESCR)
# :속성 정보:
# - 블럭 그룹의 중위수 소득
# - 블럭 그룹의 주택 연령 중위수
# - 가구당 평균 객실 수
# - 평균 가구당 침실 수
# - 모집단 블럭 그룹 모집단
# - 평균 가구원수
# - Latitude 블록 그룹 위도
# - 경도 블록 그룹 경도
# : 결측 특성 값: 없음.
print(x.shape) #(20640, 8)
print(y.shape) #(20640, )

x_train, x_test, y_train, y_test = train_test_split(
    x, y, train_size=0.6, test_size=0.2, random_state=100, shuffle=True
)
print(x_train.shape) #(14447, 8)
print(y_train.shape) #(14447,)

#2.  모델구성
model = Sequential()
model.add(Dense(100, input_dim=8))
model.add(Dense(100))
model.add(Dense(90))
model.add(Dense(80))
model.add(Dense(70))
model.add(Dense(60))
model.add(Dense(50))
model.add(Dense(40))
model.add(Dense(30))
model.add(Dense(20))
model.add(Dense(10))
model.add(Dense(1))

#3. 컴파일, 훈련
model.compile(loss='mse', optimizer='adam')
start_time = time.time()
hist = model.fit(x_train, y_train, epochs=500, batch_size=200,
          validation_split=0.2) # validation data => 0.2 (train 0.6/ test 0.2)
end_time = time.time() - start_time

#4 평가, 예측
loss = model.evaluate(x_test, y_test)
print('loss : ', loss)

y_predict = model.predict(x_test)

r2 = r2_score(y_test, y_predict)
print('r2 스코어 : ', r2)

print(end_time)

# 시각화
import matplotlib.pyplot as plt
plt.figure(figsize=(9, 6))
plt.plot(hist.history['loss'], marker='.', c='orange', label='loss')
plt.plot(hist.history['val_loss'], marker='.', c='blue', label='val_loss')
plt.title('Loss & Val_loss')
plt.ylabel('loss')
plt.xlabel('epochs')
plt.legend()
plt.show()

# result(1)
# loss : 0.5997371077537537
# r2스코어 : 0.5473926542842207
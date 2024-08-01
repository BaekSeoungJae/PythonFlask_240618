import numpy as np #넘파이 모듈을 가져오고 별칭을 np 정함
# 배열이란? 순서가 있는 같은 종류의 데이터가 저장된 집합을 의미

#튜플 data2 = (1, 2, 3, 4, 5, 6)
#튜플 data3 = 1, 2, 3, 4, 5, 6
#튜플 data4 = 1,
data = [1, 2, 3, 4, 5, 6, 7]
a1 = np.array(data) # 리스트를 넘파이 배열로 변환
print(data)
print(a1)

data2 = [0,1,2,3,4,12, 0.5, 3.14]
a2 = np.array(data2)
print(a2)

x = np.array([0.1, 0.2, 0.3])
print(x)
print(x.shape) # 배열의 형태를 나타냄
print(x.dtype) # 배열 요소의 데이터 타입을 반환 합니다.

y = np.array(([1,2,3],[4,5,6]))
print(y)
print(y.shape)
print(y.dtype)

a3 = np.arange(0, 10, 2) # 0 ~ 10 미만, 간격은 2
print(a3)

a4 = np.arange(1, 10) # 0 ~ 10 미만, 간격을 생략하면 1
print(a4)

a5 = np.arange(12).reshape(4, 3)
print(a5)
print(a5.shape) # 구성된 배열의 형태를 알아보기 위해 사용

a6 = np.linspace(1, 10, 10)
print(a6)

# 0 ~ 파이까지 동일한 간격으로 20개의 데이터를 생성
a7 = np.linspace(0, np.pi, 20)
print(a7)

# 1차원 배열
a8 = np.zeros(10)
print(a8)
# 2차원 배열
a9 = np.zeros((3, 4))
print(a9)

a10 = np.ones(5)
print(a10)

a11 = np.ones((3, 5))
print(a11)

a12 = np.eye(4)
print(a12)

a13 = np.array(['1.5', '0.62', '2', '3.14', '3.141592'])
print(a13)
print(a13.dtype) # <U8의 의미는 데이터 형식이 유니코드이며 문자의 수는 최대 8개라는 의미

num_a13 = a13.astype(float) # 문자열을 실수 타입으로 변환
print(num_a13)

a14 = np.array(['1', '3', '5', '7', '9'])
num_a14 = a14.astype(int) # 문자열을 정수 타입으로 변환
print(num_a14)

a15 = np.random.rand(2,3)
print(a15)
a16 = np.random.rand(2, 3, 4) # 3 차원 배열
print(a16)

a17 = np.random.randint(10, size=(3, 4)) # 0 ~ 9 사이의 정수
print(a17)

import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

# 요소별 덧셈
result = arr1 + arr2
print(result)

# 요소별 곱셈
result = arr1 * arr2
print(result)

# 요소별 거듭제곱
result = arr1 ** 2
print(result)

# 요소별 비교 연산 : true, flase 반환
arr3 = np.array([10, 20, 30, 40])
print(arr3 > 20)

arr4 = np.arange(5)
print(f"합계 : {arr4.sum()}, 평균 : {arr4.mean()}")
print(f"표준편차 : {arr4.std()}, 분산 : {arr4.var()}")
print(f"최솟값 : {arr4.min()}, 최댓값 : {arr4.max()}")

arr = np.array([1,2,3,4,5])

#인덱싱
print(arr[0])
print(arr[2])

# 슬라이싱
print(arr[1:4]) #[2,3,4]

x = np.arange(0., 2*np.pi, 0.1)
y = np.sin(x)
print(y)

# 2*3 크기의 2차원 배열 생성
matrix1 = np.array([[1,2], [4,5]])

matrix2 = np.array([[5,6], [7,8]])

# 행렬 덧셈
result = np.add(matrix1, matrix2)
print(result)

# 행렬 뺄셈
result = np.subtract(matrix1, matrix2)
print(result)

#행렬 곱셈
result = np.dot(matrix1, matrix2)
print(result)

#전치 행렬 : 행과 열을 교환하여 얻는 행렬이다.
matrix = np.array([[1,2,3], [4,5,6]])
result = np.transpose(matrix)
print(result)

# 역행렬 : 정방행렬 A에 대해 A와 곱했을 때 항등행렬이 되는 행렬 입니다.
matrix3 = np.array([[1,2],[3,4]])
inverse_matrix = np.linalg.inv(matrix3)
print(inverse_matrix)

x = np.array([9,8,7,2,3,4,6])
print(np.amin(x)) # 최소값
print(np.amax(x)) # 최대값
print(np.argmin(x)) # 최소값이 있는 위치
print(np.argmax(x)) # 최대값이 있는 위치
print(np.sort(x)) # 오름차순 정렬
print(np.argsort(x)) # 값의 인덱스

# 크기가 다른 배열 생성
a = np.array([1, 2, 3]) # 1차원 배열
b = np.array([[4], [5], [6]]) # 2차원 배열 (3 X 1)

# 브로드캐스팅을 사용한 배열 연산
c = a + b

print(c)
# 판다스 내장 데이터셋 타이타닉 승객 데이터 사용
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv')

print(df.info())
print(df.head())
print(df.describe())

# 결측치 확인
print(df.isnull().sum())

# 결측치 처리: Age의 결측치를 평균값으로 대체
df['Age'].fillna(df['Age'].mean(), inplace=True)

# Embarked의 결측치를 최빈값으로 대체
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# 결측치 재확인
print(df.isnull().sum())

# 새로운 열 추가: 가족 수(FamilySize)
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
print(df.head())

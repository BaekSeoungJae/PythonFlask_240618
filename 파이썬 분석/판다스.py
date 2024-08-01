import numpy as np
import pandas as pd

s1 = pd.Series([10,20,30,40,50]) # 리스트 구조로 데이터를 입력
print(s1)

s2 = pd.Series(['a', 'b', 'c',1,2,3])
print(s2)

s3 = pd.Series([np.nan, 10, 20, 30])
print(s3)

index_date = ['2023-09-15', '2023-09-16', '2023-09-17', '2023-09-18']
s4 = pd.Series([200, 195, np.nan, 205], index=index_date)
print(s4)

s5 = pd.Series({'국어': 100, '영어': 95, '수학': 90})
print(s5)

s6 = pd.date_range(start='2023-09-16', end='2023-09-30')
print(s6)

s7 = pd.date_range(start='2023-09-16', periods=4, freq='W')
print(s7)

df = pd.DataFrame({'name' : ['민지', '하니', '혜린', '다니엘', '혜인'],
                   'kor' : [90, 88, 97, 77, 92],
                   'eng' : [88, 92, 87, 96, 96]})

print(df)
print(df['eng'])
print(sum(df['eng']))
print(sum(df['eng'])/df['eng'].size)

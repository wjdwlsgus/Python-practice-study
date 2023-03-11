# 튜플 활용
tu=('a','b','c')

tu.index('c')      # 위치 찾기
'b' in tu          # 확인하기
len(tu)            # 전체 개수
tu.count('a')      # 특정 개수 세기


num=(5,7,9)
n1,n2,n3=num       # 변수 할당하기


a='hello'
b='world'
(a,b)=(b,a)        # 값 교환하기


li=['a','b','c','d','e','f']
tuple(li)          # 리스트 -> 튜플

tu=('a','b','c')
list(tu)           # 튜플 -> 리스트

# 최소값 구하기
li=list(map(int,input('숫자 입력:').split()))

m=li[0]

for i in li:
    if i<m:
        m=i
        print(m)

# 최대값 구하기
li=list(map(int,input('숫자 입력').split()))

m=li[0]

for i in li:
    if i>m:
        m=i
        print(m)
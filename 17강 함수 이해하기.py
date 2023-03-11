# 함수란?
# 프로그램을 짤 때 효율을 높이기 위하여 특정 기능을 미리 만들어두고 이름을 붙여 사용


# 함수 정의하기  인자값/리턴값이 있을경우와 없을 경우

# 둘다 없는 경우
def aa():
  print('hi~')
# 인자값은 있는 경우
def bb(x):
  print('hello~')
# 리턴값만 있는 경우
def cc():
  n=int(input('n'))
  print(n*2)
  return n*2
# 리턴값과 인자값 모두 있는 경우
def dd(x,y):
  print(x*y)
  return x*y

# 함수 호출하기
 
re1 = aa()
re2 = bb(3)
re3 = cc()
re4 = dd(3,5)


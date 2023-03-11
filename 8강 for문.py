# for문

for i in range(10):
  print(i)

# 1에서 n까지 출력

n=int(input('n:'))

for i in range(1,n+1):
  print(i)

# a에서 b까지 출력
a,b=map(int,input('a,b:').split())

for i in range(a,b+1):
  print(i)

# n에서 0까지 출력

n=int(input('n:'))

for i in range(n,-1,-1):
  print(i)
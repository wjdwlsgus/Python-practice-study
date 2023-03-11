# while 문
print('a가 0보다 같거나 크면 실행, 작으면 정지')
a=int(input('a:'))

while a>=0:
  print('실행')
  a=int(input('a'))
  
# 무한루프
a= 10

while a>0:
  print('실행')

#n번 반복하기
n=int(input('n:'))
    
while n:
  print(n)
  n=n-1

# ~까지 반복하기
# 1~10까지 반복하기
n=1
while n<=10:
  print(n)
  n=n+1

# yes를 입력하면 반복하기
text='yes'

while text=='yes':
  text=input('yes 입력 시 반복')

print('종료')


    
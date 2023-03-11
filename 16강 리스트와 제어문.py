# for문으로 리스트 값 추가
li=[]

for i in range(5):
  li.append(int(input('숫자 입력:')))

# for문으로 리스트 값 출력
li = [5,3,8,6,1]
for i in range(len(li)):
  print(li[i])


for i in li:
  print(i)


# if문 추가
for i in range(len(li)):
  if i%2==0:
    print(li[i])    


for i in li:
  if i%2==0:
    print(i)


# 리스트 분리하기
li=list(input('문자 입력:'))

up=[]
low=[]

for i in li:
  if i.isupper():
    up.append(i)
  elif i.islower():
    low.append(i)
print(up)
print(low)

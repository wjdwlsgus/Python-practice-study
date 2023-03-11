# if
num=int(input('숫자 하나 입력:'))

if num>0:
  print('{}은 양수입니다.'.format(num))

# if ~else
num=int(input('숫자 하나 입력:'))

if num%2==0:
  print('{}은 짝수입니다.'.format(num))
else:
  print('{}은 홀수입니다.'.format(num))

#if ~elif
age = int(input('나이 입력:'))

if age<=7:
  print('유아입니다')
elif age<=19:
  print('청소년입니다.')
elif age >= 20:
  print('성인입니다.')
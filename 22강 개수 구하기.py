# 약수의 개수 구하기
# n을 입력받아 n의 약수의 개수 구하기
n = int(input('n'))

check = 0

for i in range(1,n+1):
    if n % i == 0:
        check = check + 1
print(check)

# ox 개수 구하기
#text를 입력받아 o의 개수 , x의 개수 구하기
text = list(input('text'))

o_count=0
x_count=0

for i in text:
    if i == '0':
        o_count=o_count+1
    elif i == 'x':
        x_count = x_count+1
print(o_count)
print(x_count)
#평균 이상 개수 구하기
# 여러개의 숫자를 입력 받아 평균을 구하고
# 평균 이상의 숫자 개수 구하기

num = map(int,input('num').split())

avg = sum(num)/len(num)

check = 0

for i in num:
    if i >= avg:
        check = check+1
print(avg)
print(check)
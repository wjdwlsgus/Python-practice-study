# 문자 입력받아 공백 기준 자르기
li1 = input('문자 입력').split()

# 문자 입력받아 전체 자르기
li2 = list(input('문자 입력'))

# 숫자 하나씩 입력받기
li3=[]

li3.append(int(input('숫자 입력')))
li3.append(int(input('숫자 입력')))
li3.append(int(input('숫자 입력')))


# 숫자 여러개 입력받기
li4=list(map(int,input('숫자 입력').split()))

a=input('숫자 입력').split()
b=map(int,a)
c=list(b)


# 합, 평균, 최소값, 최대값, 중간값
num=list(map(int,input('숫자 입력').split()))

num.sort()

print('합:',sum(num))
print('평균:',sum(num)/len(num))
print('최소값:',num[0])
print('최대값:',num[len(num)-1])
print('중간값:',num[len(num)//2])

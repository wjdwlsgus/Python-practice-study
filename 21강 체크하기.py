# 문자 체크
# 긴 문장(text)과 한 문자(t)를 입력받아 
# t가 text안에 포함되어 있는지를 확인

text = input('text')
t = input('t')

check = False

for i in text:
    if i == t:
        check = True
print(check)


# 숫자 체크 
# 5개의 숫자를 입력받아 리스트를 만들고
# n을 입력받아 리스트 값에 n이 있는지 확인

li = list(map(int,input('li').split()))
n = int(input('n'))

check = False

for i in li:
    if i == n:
        check = True
print(check)
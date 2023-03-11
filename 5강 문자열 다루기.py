# 문자열 인덱스

text='abc'

print(text[0]) # text[-3] == text[0]
print(text[1]) # text[-2] == text[1]
print(text[2]) # text[-1] == text[2]

# 문자열 슬라이스
text='abcde fgh ijk'

print(text[2:5])
print(text[1:8])
print(text[-5:-1]) 
print(text[0:12:2])

# 문자열 메서드
text = 'abcde {} {}'
print(text.format('ABC', 123))

# 2. 대체하기 : replace(a,b)
text = 'abcde ABC ABC'
print(text.replace('A','K'))

#4. 합치기 : a.join()
text = 'abcde'
print('/'.join(text))

#5. 개수 확인하기 : count(a)
text = 'abcde ABC ABC'
print(text.count('a'))
print(text.count('A'))
print(text.count('1'))


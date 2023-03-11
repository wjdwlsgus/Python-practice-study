# 딕셔너리 만들기
dic = {}
dic = dict()


# 딕셔너리 특징
dic = {'kor':80,'eng':90,'mat':77}
dic['kor'] 
# 인덱스값으로 불러오는게 아닌 키값으로 불러온다
dic['kor']=85
# 변경된 값은 바뀐다
dic['sci']=92
# 없던 값은 추가된다


# 딕셔너리 활용

del dic['mat']       # 삭제하기
dic.clear()          # 전체 삭제
'eng' in dic         # 확인하기 (키 기준)
len(dic)             # 전체 개수     

dic.keys()           # 모든 키 얻기
dic.values()         # 모든 값 얻기
dic.items()          # 모든 순서쌍얻기

tuple(dic)    # 바뀔때 키값만 들어간다
list(dic)
set(dic)

li=['ab','cd','ef'] 
dic(li)   # 딕셔너리를 만들려면 짝이 맞아야한다

li=[['a',1],['b',2],['c',3]]
dic(li)

li=[['a',1],['b',2],['c',3]]
dic(li)
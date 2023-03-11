# 기타 제어문

#continue 해당 단계만 건너뛰고 다음 단계로 간다.
for i in range(1,11):
  if i==5:
    continue
  print(i)

#break 제어문을 중단하고 빠져나간다
for i in range(1,11):
  if i==5:
    break
  print(i)

#pass 아무 작업도 하지 않는다.
for i in range(1,11):
  if i==5:
    pass
  print(i)
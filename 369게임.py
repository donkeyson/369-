start, end = map(int, input("시작값과 종료값을 입력하세요 : ").split())
num = start 	#시작값을 현재숫자에 입력
cnt = 0		#총 박수값
while num <= end:	#369게임 시작
  for _ in range(10):	#10번씩 반복
    if num > end: break	#종료값 초과시 강제종료
    str_num = str(num)
    if '3' in str_num or '6' in str_num or '9' in str_num:	#369 포함시
      d = 0
      d += str_num.count('3')
      d += str_num.count('6')
      d += str_num.count('9')
      cnt += d		#총 박수값 더하기
      print(f"{'*' * d:<5}", end ="")
    else:	#369 미포함시
        print(f'{num:<5}', end="")
      
    num += 1
  print('')	#줄바꿈
print(f'count = {cnt}')

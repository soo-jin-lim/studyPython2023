#연산자
#할당연산 assignment
# 2 = 1(x)
val = 1 #왼쪽에는 무조건 변수

#equal 연산자 비교해서 보는 연산자
print(1 == 1)

# 사칙연산
print(1+1)
print(10 * 10)
print(1024 / 2) # 소수 나누기
print(1024 // 2) # 정수 나누기
print(6 // 3)
print(6 % 3) # 나머지 3으로 나눴을 때 3의배수면 0임(배수를 찾을 때 유용)

#print(6 / 0)
#print(6 // 0) 
print(2 ** 10) #2의 10승

#문자열 연산
first = 'Hello'
second = 'world'
print(first + second)
print(first + ' ' + second)
print(first,second)

print(first * 4)

print(len(first)) #문자열 길이
#print(first[0])
#print(first[1])
#print(first[2])
#print(first[3])
#print(first[4])
#print(first[5]) 에러

#파이썬에서 인덱스를 찾는 특이한 방법
print(first[-1])
print(first[-2])
print(first[-3])
print(first[-4])
print(first[-5])

current = '2023-01-31 15:14:02' #현재시간
print(len(current))
print(current[0:4])#0부터 4까지
print(current[5:7])
print(current[8:10])
print(current[11:13])
print(current[14:16])
print(current[17:])

#print(current[0:4] + '년' + current[5:7] + '월' current[8:10] + '일' +
#current[11:13] + '시' + current[14:16] + '분' + current[17:] + '초' )

print(current[-19:-15])

#리스트 연산
que = [1, 2, 3, 4, 5]
que[0] = 7

print(que)

que.append(10) # 맨 마지막에 추가
print(que)

que.insert(3, 99) #특정 인덱스에 추가
print(que)

que.remove(99) # 해당 값 삭제
print(que)

#이런거 안됨
#tup = (1, 2, 3, 4, 5)
#tup[1] = 9

#print(tup)

#문자열 리스트 == 문자 리스트
title = 'python'
print(title[0])

#title[0] = 'p' # 문자열에서는 값 변경 x
print('P' + title[1:])

#일반적인 문자형 리스트
text = ['p', 'y', 't', 'h', 'o', 'n']
print(text)
text[0] = 'p'
print(text)

#문자열 포맷팅
print("I'm so happy{0} to you, {1}!!".format(2, 'Hey'))
#최신식 문자열 포맷팅
preword = 3
sayHello = 'Hey'
print(f"I'm so happy{preword} you,{sayHello}!!")

pi = 3.141592
print(f'파이는 {pi}입니다')
print(f'파이는 {pi:0.2f}입니다.')
print(f'파이는 {pi:10.3f}입니다.')

# 문자열을 특정문자로 자르기
full_name = 'Soo Jin'
vals = full_name.split() # 스페이스
print(type(vals))
print(vals)

vals = full_name.split('.')  # .으로 지정
print(vals)

print(full_name.replace('Soo', 'Ashely'))

#문자열 공백 없애기
hi = '          Hello~ Bye           '
print(hi.lstrip() + '|') # 앞의 공백을 없애는 것
print(hi.rstrip() + '|') # 오른쪽의 공백을 없애는 것
print(hi.strip() + '|')  # 좌우의 공백을 없애는 것

print(full_name.index('i'))

print(full_name.find('z'))# 찾는게 없으면 -1
print(full_name.find('G'))

#찾는 단어의 갯수를 알려줌
print(full_name.count('u'))

#모든 단어를 대문자/소문자로 변경 
print(full_name.upper())
print(full_name.lower())

#연산자 우선순위
print(3 + 4 * 2)
print((3 + 4) * 2) #먼저하고 싶은 연산은 괄호로 묶는다.
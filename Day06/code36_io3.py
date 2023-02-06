# 콘솔 출력 보충
#이스케이프 캐릭터(탈출문자)
print('1.Hello\r\nworld')
print('2.Hello\nworld') #이걸 권장

print('3.Hello\n\tworld')  #t는 탭
print('4.Hello\n\t\bworld') # b는 백스페이스
print('5.Hello\n\'world\'') # 문자열내 홑따옴표
print('6.Hello "world"') #
print('7.Hello. \"world\"')
print('8.Hello. \\world') # \를 문자열에 표현
print('9.Hello\0')

#문자열 포맷팅- 예전방식
# %로 포맷코드 시작
me = '저'
name = '임수진'
age = 24

print('%s는 %s 입니다. %d살 입니다'%(me, name, age))
print(f'{254.112233:.2f}')# 최신식 방식
print('%4.4f' %(254.112233))# 구식 전체 자리수. 소수점 
print()



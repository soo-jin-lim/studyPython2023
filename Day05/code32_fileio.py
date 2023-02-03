# ASCII -> 한단어를 표현하는 체계(영어)
# Unicode(UTF-8) - > 모든 나라언어 다 표현가능
# 파일 만들기

file = open('../sample07.txt', 'w', encoding = 'utf-8') # 파일 쓰기로 만듦

file.write('안녕하세요~\n')
file.write('첫번째 파일임\n')
file.write('절대경로에 파일이 생성될겁니다.\n')

file.close()
print('sample.txt가 생성되었습니다.')


#파일/폴더 경로

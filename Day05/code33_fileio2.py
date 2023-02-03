#파일 읽어오기
file = open('./Day05/sample05.txt','r',encoding='utf-8')


while True:
    text = file.read()

    if not text: break
    print(text)

file.close() #파일을 열었으면 무조건 닫아줘라
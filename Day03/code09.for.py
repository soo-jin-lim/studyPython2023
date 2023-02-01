# for문
arr = [1,2,3,4,5]
sum = 0

for item in arr:
    print(item)
    # print(f'{item:2.2f}')
    sum = item # SUM = SUM + ITEM 
    print('합계는  ', sum)

#리스트를 맘 편히 만드는 방법
VALS = [i for i in range(1,11)]
print(VALS)

#continue / break
num = 0
for item in VALS:
    num += 1
    if num % 2 == 0:
        #continue #이후의 것을 수행하지않고 다시 for문으로 가는 것
        break # break를 만나면 for문을 완전히 탈출 if만 썼을 때는 사용 불가능 for를 같이 사용해야함.
    else:
        print(num, '번 수는 ',item, '입니다')





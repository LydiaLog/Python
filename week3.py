# 20215196 윤지원
# 10번 문제
first = int(input('첫 번째 수를 입력하세요 : '))
second = int(input('두 번째 수를 입력하세요 : '))

print(first /second) 

a = int(first//second)
b = int(first%second)
c = (a,b)

print('몫과 나머지는 각각', c, '입니다.' )

#11번 문제
sec = int(input('초 : '))
                
print('%d초 = %d 분 % d 초' % (sec, sec//60, sec%60))

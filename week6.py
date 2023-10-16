# 윤서은 20215196

while True:
    sum = 0
    x = int(input('정수 입력: '))
    
    if (x < 1):
        print('1보다 작은 수를 입력하여 종료했습니다.') 
        break
    
    for n in range(1, x+1):
        print(n, end=' ')
        sum += n
        
    print('sum = ', sum)    
    
  
    

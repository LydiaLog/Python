# 윤서은 20215196

while True:
    
  first = int(input("정수 입력 : "))
  cal = str(input("연산자 입력 : " ))
 

  if cal == '+' :
     second = int(input("정수 입력 : "))
     print(first, cal, second, '=', first + second)
    
  elif cal == '-' :
     second = int(input("정수 입력 : "))
     print(first, cal, second, '=', first - second)
        
  elif cal == '*' :
     second = int(input("정수 입력 : "))
     print(first, cal, second, '=', first * second)

  else:
    print("연산자를 잘못 입력하셨습니다.")
    break
    
    
    
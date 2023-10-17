#윤서은 20215196
data = []

while True:
    
   str = input("문자열 입력: ")
    
   if( str == ''):
      break
    
   data.append(str)
   new_data = sorted(data) 
   
print('data =', data)


print('알파벳 순서로 정렬' ,'\ndata=', new_data)

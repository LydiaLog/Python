# 윤서은 20215196

def val_change(data, val, chg):
    flag = False
    
    for i in range(len(data)):
         if(data[i] == val):
             flag = True
             data[i] = chg
            
            
    return(data, flag)
data = ['python', 'c', 'java', 'c++', 'swift', 'r']

print('>>>')
while True:

        print('---------------------------------------------')
        print(data)


        val = input(' -> 변경하고 싶은 값: ')

        chg = input(' -> 변경 할 값: ')
    
       
 
        (data, flag) = val_change(data, val, chg)
 

        if(not flag):

            print(' -> 자료가 일치하지 않아 프로그램을 종료합니다.')

            break
print('>>>')
# 윤서은 20215196
price = {'apple':200, 'banana':300, 'grape':500}
count = {'banana':4, 'grape':2, 'apple':3}

for item in price:
    print (item +  str(price[item]) + '원 ' +  str(count[item]) + '개')

a = price['apple'] * count['apple']
b = price['banana'] * count['banana']
c = price['grape'] * count['grape']
print ('총합 = ' , a + b + c)
    
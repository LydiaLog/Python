#윤서은 20215196
import random

num = random.sample(range(1,51),10)
print('num=', num)

fives = [] 

for i in num:
    if i % 5 == 0: 
       fives.append(i) 

print('fives =', fives)     

#윤서은 20215196
midtest={'benny':80, 'daniel':98, 'joon':100}

class_06=['daniel', 'joon']

sum = 0.0
count = 0

print('중간고사에서 06분반 학생들의 성적')

for m in class_06:
    print('  -> ', m, ' = ', midtest.get(m))
    sum += midtest[m]
    count += 1

print('06분반 중간고사 반평균 = %.2f' %(sum/count))        
        
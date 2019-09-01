'''

    Prototype of a virtual doctor. 
    
    author : ritesh_vesalapu
    date   : 04-06-2019
    mentor : Saurabh sir


'''

import datetime
def generate_report(name,dis):
    print()
    print(name.capitalize()+"'s report")
    print('Date : ' + str(datetime.date.today()))
    now = datetime.datetime.now()
    print('Time : ' + now.strftime("%H:%M:%S"))
    print('Disease : '+ dis )
    print('Medicine : ' )
    

sym_list = ['sym1','sym2','sym3','sym4','sym5','sym6','sym7','sym8','sym9']
dis_list = ['dis1','dis2','dis3','dis4']
med_list = ['med1','med2','med3','med4','med5','med6']
final_dis = {}


user_name = input('Enter your name: ')
print('Welcome ' + user_name.capitalize() +'!')

import random
for i in range(len(dis_list)):
    random.shuffle(sym_list)
    temp_list=list(sym_list[:3])
    final_dis[dis_list[i]] = temp_list
sym_user = list(input('Enter the symptom: ') for i in range(3))
# print(sym_user)
count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0
for i in sym_user:
    if i in final_dis['dis1']:
        count_1 = count_1+1
    if i in final_dis['dis2']:
        count_2 = count_2+1
    if i in final_dis['dis3']:
        count_3 = count_3+1
    if i in final_dis['dis4']:
        count_4 = count_4+1
res = max(count_1,count_2,count_3,count_4)
if res == count_1:
    random.shuffle(med_list)
    user_medlist = list(med_list[:2])
    dis = 'dis1'
    print('You are diagnosed with '+'dis1.')
    print('Please use the medicines as directed: ')
    for i in range(len(user_medlist)):
        dose_v = str(random.randint(1,3))
        print(str(random.randint(1,3))+' of '+user_medlist[i])

elif res == count_2:
    random.shuffle(med_list)
    user_medlist = list(med_list[:2])
    dis = 'dis2'
    print('You are diagnosed with '+'dis2.')
    print('Please use the medicines as directed: ')
    for i in range(len(user_medlist)):
        print(str(random.randint(1,2))+' of '+user_medlist[i])
    
elif res == count_3:
    random.shuffle(med_list)
    user_medlist = list(med_list[:2])
    dis = 'dis3'
    print('You are diagnosed with '+'dis3.')
    print('Please use the medicines as directed: ')
    for i in range(len(user_medlist)):
        print(str(random.randint(1,3))+' of '+user_medlist[i])
elif res == count_4:
    random.shuffle(med_list)
    user_medlist = list(med_list[:2])
    dis = 'dis4'
    print('You are diagnosed with '+'dis4.')
    print('Please use the medicines as directed: ')
    for i in range(len(user_medlist)):
        print(str(random.randint(1,2))+' of '+user_medlist[i])

choice = int(input('Do you want to generate your report: 1.Yes    2.No'))
if choice == 1:
    generate_report(user_name,dis)
elif choice == 2:
    pass


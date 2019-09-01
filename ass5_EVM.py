'''

    Prototype of an EVM.
    Includes user and admin login,vote limitation, one_time voting system. 
    
    author : ritesh_vesalapu
    date   : 04-06-2019
    mentor : Saurabh sir

'''

def login(s):
    if s == 'a':
        flag = 1
        while(flag!=0):
            while(True):
                user = input('Enter your username: ')
                if int(user) in admin_u:
                    pass
                else:
                    print('Invalid username')
                    break
                passw = input('Enter your password: ')
                if (int(user),passw) in list(zip(admin_u,admin_p)):
                    print('Login successful.')
                    flag = 0
                    login_v = 1
                    return login_v
                    break
                    
                else:
                    print('Incorrect password.Please try again.')
                re = int(input('Do you want to try again? '))
                if re == 1:
                    continue
                else:
                    flag = 0
                    break
                
    if s == 'u':
        flag = 1
        while(flag!=0):
            while(True):
                user = input('Enter your username: ')
                if (int(user) in user_u) and (not(int(user) in voted_user)):
                    pass
                elif int(user) in voted_user:
                    print('Already voted')
                    break
                else:
                    print('Invalid username')
                    break
                passw = input('Enter your password: ')
                if (int(user),passw) in list(zip(user_u,user_p)):
                    print('Login successful.')
                    flag = 0
                    login_v = 2
                    voted_user.append(int(user))
                    return login_v
                    break
                    
                else:
                    print('Incorrect password.Please try again.')
                re = int(input('Do you want to try again? '))
                if re == 1:
                    continue
                else:
                    flag = 0
                    break
                
admin_u = [123,456,789]
admin_p = ['abc','def','ghi']
user_u = [1234,4567,7890,9123]
user_p = ['abcd','defg','ghij','jklm']
voted_user = []
login_v = 0
user_count = 0
choice = -1
a_count,b_count,c_count,d_count,n_count = 0,0,0,0,0
while(True):
    print('Please select login mode: ')
    print('1.Admin login    2.User login')
    choice = int(input('Enter your choice: '))
    results = (a_count,b_count,c_count,d_count,n_count)
    result_list = list(results)
    party_list = ['A','B','C','D','NOTA']
    if choice == 1:
        login_v = login('a')
        if login_v == 1:
            admin_choice = -1
            print('1.Enter vote count    2.See Results')
            admin_choice = int(input('Please select the operation: '))
            if admin_choice == 1:
                vote_co = int(input('Enter the vote count for today: '))
            elif admin_choice == 2:
                for i in range(len(list(results))):
                    print(party_list[i] +' : '+ str(result_list[i]),end = '    ')
                print()
            continue
        else:
            print('Please login first.')
    elif choice == 2:
        if user_count<vote_co:
            login_v = login('u')
            if login_v == 2:
                user_count += 1
                print('Welcome User.')
                print('1.party_A    2.party_B    3.party_C    4.party_D    5.NOTA')
                vote_choice = int(input('Please cast your vote: '))
                if vote_choice == 1:
                    a_count += 1
                elif vote_choice == 2:
                    b_count += 1
                elif vote_choice == 3:
                    c_count += 1
                elif vote_choice == 4:
                    d_count += 1
                elif vote_choice == 5:
                    n_count += 1
        else:
            print('Vote limit reached!!')
    else:
        print('Invalid choice')



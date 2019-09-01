u = [123, 456, 789]
p = ['abc','def','abc']
amount = [5000,2000,3000]
while(True):
    while(True):
        user = input('Enter the username: ')
        passw = input('Enter the password: ')
        login = 0
        ##for i in range(3):
        ##    if u[i] == int(user) and p[i] == passw:
        ##        print('Login success')
        ##else:
        ##    print('Please check your login credentials')
        lf = list(zip(u,p))
        ##print( (user,passw))
        if (int(user),passw) in lf:
            print('Login success')
            login = 1
            break
        else:
            print('Login failed. Please re enter your details.')
            
            

    if login==1:
        print('Please choose the operation: ')
        print('1.Withdrawl 2.Deposit 3.Balance_check 4.pin_change')
        choice = int(input('Enter your choice: '))
        if choice == 1:
            cashw = int(input('please enter the amount to withdraw: '))
            if cashw<amount[u.index(int(user))]:
                print('please collect your cash')
                amount[u.index(int(user))] = amount[u.index(int(user))]-cashw
            else:
                print('Insufficient balance')
        elif choice == 2:
            cashd = int(input('Enter the cash to be deposited: '))
            amount[u.index(int(user))] = amount[u.index(int(user))]+cashd
            print('Your updated balance is: ' ,amount[u.index(int(user))])
        elif choice == 3:
            print('your balance is : ' ,amount[u.index(int(user))])
        elif choice == 4:
            oldpass = input('Enter the old password: ')
            if oldpass == p[u.index(int(user))]:
                newpass = input('Enter the new password: ')
                p[u.index(int(user))] = newpass
                print('Your password is updated')
            else:
                print('Incorrect password')
        re = int(input('Do you want to do anything else? '))
        if re == 1:
            continue
        else:
            break

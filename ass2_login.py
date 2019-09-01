
courses = ['TN-ML','TN-IoT']
while(True):
    while(True):
        name = input('Enter your name: ')
        res = [name]
        email = input('enter your email id: ')
        if '@' in email:
            pass
        else:
            print('Invalid email')
            break
        res.append(email)
        mobile = input('Enter your contact no: ')
        if len(mobile)==10:
            pass
        else:
            print('Invalid mobile no')
            break
        res.append(mobile)
        course = input('Enter the course preferred: ')
        if course in courses:
            res.append(course)
            pass
        else:
            print('Please check the course list')
        break
    if len(res) == 4:
        pass
    else:
        re = int(input('Do you want to re enter'))
        if re == 1:
            continue
        else:
            break
    break
if len(res) == 4:
    print(res)

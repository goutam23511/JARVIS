from datetime import datetime


def boot_system():
    print(f'INITIALIZING SYSTEM.......')

    user_time=datetime.now().strftime(f'%I:%M %p')

    print(f'[ACCESSED TIME] {user_time}')

    attempts=0
    while True:
        pin=int(input(f'Enter the pin: '))
        attempts+=1

        if pin==230511: 
            print('Access granted! Welcome sir what would you want me to do today?')
            break 

        elif attempts==4:
            print(f'Access denied')
            exit()

        
    

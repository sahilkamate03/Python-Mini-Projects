import random
nu=str(random.randint(100,999))
n=list(nu)
print()
print(' Number Guessing Game.')
print('\n Pico: You guessed correct digit but in wrong place. \n Fermi: You guessed correct digit in right place \n Bagel: You havent guessed any number correct')
print()
print('You have only 10 chances')
print()
print('*'*30)
c=1
while True:

    if c>10:
        print()
        print('*'*30)
        print(f'You lost. Better luck nxt time. \n The number was {nu}')
        print('*'*30)
        print()
        break

    i = str(input(f'{c}. Enter 3 digit number: '))

    if len(i)!=3:
        print('-'*30)
        print('Please enter 3 digit number.')
        print('-'*30)
        continue
    
    a=list(i)

    if n==a:
        print('you guessed the correct number ')
        print('+-'*30)
        print(f'You guessed the number in {c} chances!!')
        print('+-'*30)
        break
    
    else:
        for i in range(len(n)):
            if a[i]==n[i]:
                print('*'*30)
                print('Fermi')
                print('*'*30)
                next=True
                break
            
            else:
                next=False
                
        if next==False:
            for i in range(len(n)):

                if next == False:
                    if a[i] in n:
                        print('*'*30)
                        print('Pico')
                        print('*'*30)
                        next=True
                        break

                    else:
                        next=False

                else:
                    print('*'*30)
                    print('Bagel')
                    print('*'*30)
        
        c+=1
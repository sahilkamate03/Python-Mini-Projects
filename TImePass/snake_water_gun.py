import random
option=['Snake','Water','Gun']
win=chances=0
play=int(input('Enter the no of times u want to play: '))
try:
    while chances<play:
        chances+=1
        print('1.Snake\t\t2.Water\t\t3.Gun')
        hand=int(input("Enter the choice(1/2/3): "))
        d=hand-1
        selected=random.choice(option)
        print(f"Computer chosses: {selected}",end='\n')
        if d==option.index(selected):
            print('Draw')
        else:
            if d==0:
                if option.index(selected)==1:
                    print('You Win!! ')
                    win+=1
                else:
                    print('Computer Win')

            if d==1:
                if option.index(selected)==2:
                    print('You Win!! ')
                    win+=1
                else:
                    print('Computer Win')
            if d==2:
                if option.index(selected)==0:
                    print('You Win!! ')
                    win+=1
                else:
                    print('Computer Win')
        print()
except:
    print("Plz try Again.A problem occured.")

print()
print(" No of chances played: ",chances,"\n","No of wins: ",win)

if chances-win>win:
    print("Computer wins the match. Better luck nxt time.")

elif chances-win<win:
    print("You succesfully defeated the computer!!! \n Well done.")
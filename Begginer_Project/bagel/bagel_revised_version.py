import random

NUM_DIGITS=3
MAX_GUESSES=10

def main():
    print('''
    Bagel Game!! (Made by Sahil Annaso Kamate)
    
    When I say      What it means
    
    Pico            One digit is correct but in wrong postion
    Fermi           One digit is correct in the right postition
    Bagel           No digit is correct
    ''')

    while True:
        secretNum=getSecretNum()

        print(f'I have thought a {NUM_DIGITS} digit number')
        print(f'You have {MAX_GUESSES} chances')

        numGuesses=1

        while numGuesses<=MAX_GUESSES:
            guess=''
            while len(guess)!=NUM_DIGITS or not guess.isdecimal() :
                print(f'Guess #{numGuesses}')
                guess=input('> ')
            
            clues=getClues(guess,secretNum)
            print(clues)
            numGuesses+=1

            if guess==secretNum:
                print('You guessed the number correct.')
                break

            if numGuesses>MAX_GUESSES:
                print(f'You ran out of chance. The number was {secretNum}')
                break
        
        print('Do you want to play again? (yes/no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for Playing')

def getSecretNum():
    numbers=list('1234567890')
    random.shuffle(numbers)
    secretNum=''
    for i in range(NUM_DIGITS):
        secretNum+=numbers[i]
    return secretNum

def getClues(guess,secretNum):
    if guess==secretNum:
        return 'You got it right!'

    clues=[]

    for i in range(len(guess)):
        if guess[i]==secretNum[i]:
            clues.append('Fermi')
        
        elif guess[i] in secretNum:
            clues.append('Pico')

    if len(clues)==0:
        return 'Bagels'

    else:
        clues.sort()    
        return ' '.join(clues)

if __name__=='__main__':
    main()
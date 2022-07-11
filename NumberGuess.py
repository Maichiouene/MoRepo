import random 

def guess(x):
    random_number= random.randint(1,x)
    guess= 0
    i=0
    while (guess != random_number):  
        guess= int( input(f'Guess a number between 1 and {x}: '))
        if (guess < random_number):
            print('Too low, guess again')
        elif (guess > random_number):
            print('Too high, guess again')
        
        print('Guess again!')
        i=i+1
    print(f'Congrats! You finally got it, the correct number was {random_number}, it took you {i} tries')


#guess(10)



def computer_guess(x):
    low=1
    high=x
    feedback= ''

    while feedback!= 'c' :
        if low!= high:
            guess=random.randint(low,high)
        else:
            guess=low 

        feedback=input(f'The computer guessed {guess}, is this too High (H), too Low (L), or correct (C)??').lower()
        if feedback=='h':
            high= guess-1
        elif feedback=='l':
            low=guess+1

    print(f'Computer guessed correctly, {guess}, ') 



computer_guess(50)
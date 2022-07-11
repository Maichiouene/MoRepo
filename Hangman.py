
import random
import string 
from Words import words 



eat=2 
def get_valid_word(words):
    word=random.choice(words) # Get a random word from this loop 
    while '-' in word or ' ' in word:
        word=random.choice(words) 

    return word.upper()

def hangman():
    word=get_valid_word(words)
    word_letters=set(word)
    alphabet=set(string.ascii_uppercase)
    used_letters=set()

    lives=6
    while len(word_letters)>0 and (lives>0):
        print('You have ',lives,' lives left ','You have used these letters: ', ' '.join(used_letters))    

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('current word:', ' '.join(word_list)) 

        user_letter=input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives=lives-1
                print(f'Letter not in the word, you have {lives} left.')
        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')

        else: 
            print('Invalid character. Please try again')
    return f'You did it! The word was {word}'


print(hangman())

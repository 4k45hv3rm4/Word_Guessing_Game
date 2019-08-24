import random
#list of words
word = ["lemon","mango","banana","apple"]
#ask Name
name= ("Hi !Enter  Your name")
print(f"Hi {name} , Let's start the game")

choice='y'
while(choice == 'y'):
    print("\t\t ***Word Guessing Game*** ")
    print("You have 10 attempts to guess the word correctly .")

    #list to store wrong guessed_letters
    wrong_list=[]
    #generate random word
    original_word=random.choice(word)

    print(f"The word is of {len(original_word)} letters. ")

    #create an empty list
    guessed_word = []
    for i in range(len(original_word)):
        guessed_word.append("__")
    print(*([i for i in guessed_word]))
    c=8
    while(c):
        c=c-1

        #take input from user
        guessed_letter = input("Guess the  letter")
        #check if guessed_letter is an alphabet
        if not guessed_letter.isalpha():
            print('Guess only a letter')
        #check if guessed letter length is one or not
        elif(len(guessed_letter)>1):
            print('Guess only one letter...')
        #check that letter choosen by user is already guessed or not
        elif(guessed_letter in wrong_list):
            print('You have Already guessed this letter')

        #check if guessed_letter is matches with original_word
        if guessed_letter in original_word:
            for i in range(len(original_word)):
                if original_word[i] == guessed_letter:
                    guessed_word[i]=original_word[i]

        else:
            #if gussed_leete is not in original_word , prompt user for wring choosen letter
            print("You Guessed wrong letter")
            wrong_list.append(guessed_letter)

        print(guessed_word)
        guess_word = [i for i in guessed_word]
        guess_word = "".join(guess_word)
        print(guess_word)
        if original_word ==guess_word :
            print('YAY !!, You have Got the letter ...')
            exit(0)
        #print the gussed word
        print(*([i for i in guessed_word]))
        #prompt user showing number of attempts left to win
        print(f"You have {c} attempts left")
        if c==0:
            if  original_word!=guessed_word  :
                print(f"You lost the game ,The original Word was {original_word}")
                exit(0)


import random
def main():
    words = ["mainstream","stage","hot","tap","pull","elephant","road","steward","tumour","admire","sermon","pattern","lamb","publisher","march","tell","bar","activity","buffet","wrong"]

    hangman = random.choice(words)
    start()
    print('The length of the word is: ' + str(len(hangman)))
    print(" ".join(lines(hangman)))
    guess(hangman)

def start():
    print('''
---------+
   |     |
   |     |
         |
         |
---------+''')

def lines(hangman):
    i = int(0)
    linesPrint = []
    while i < len(hangman):
        linesPrint.append('_')
        i = i + 1
    return linesPrint

def findLetters(lettersGuess, hangmanSplit):
    if not hangmanSplit:
        return 0
    elif hangmanSplit[0] == lettersGuess:
        return True
    elif findLetters(lettersGuess, hangmanSplit[1:]):
        return True
    else:
        return False

def progess(attempts):
    if attempts == 0:
        print('''
---------+
   |     |
   |     |
   0     |
         |
         |
         |
---------+''')    
    elif attempts == 1:
        print('''
---------+
   |     |
   |     |
   0     |
   |     |
         |
         |
---------+''')
    elif attempts == 2:
        print('''
---------+
   |     |
   |     |
   0     |
  /|     |
         |
         |
---------+''')
    elif attempts == 3:
        print('''
---------+
   |     |
   |     |
   0     |
  /|\\   |
         |
         |
---------+''')
    elif attempts == 4:
        print('''
---------+
   |     |
   |     |
   0     |
  /|\\   |
  /      |
         |
---------+''')
    elif attempts == 5:
        print('''
---------+
   |     |
   |     |
   0     |
  /|\\   |
  / \\   |
         |
---------+''')
        print('You are dead')
        print("You lost the game.")
        print("Do you want to replay?")
        response = (input()).lower()
        if(response == 'yes'):
            main()
        else:
            exit(0)

def correctAnswer(lettersGuess, hangmanSplit,rep):
    i = int(0)
    while i < len(hangmanSplit):
        if(lettersGuess == hangmanSplit[i]):
            rep[i] = lettersGuess
        i = i + 1
    print("".join(rep))
    if(rep == hangmanSplit):
        print("You have won. Great")
        exit(0)

def guess(hangman):
    rep = lines(hangman)
    hangmanSplit = list(hangman)
    lettersGuess = " "
    increase = 0
    while True:
        lettersGuess = input("Your guess: ")
        if(findLetters(lettersGuess,hangmanSplit)):
            correctAnswer(lettersGuess,hangmanSplit,rep)
        else:            
            progess(increase)
            increase = increase + 1
main()
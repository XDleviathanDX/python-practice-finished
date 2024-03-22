import random
#ramdomises choices

name = input("what is your name?")
#user is asked for name

print("good luck!", name)

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

# function will choose one random word

word = random.choice(words)

print("guess the characters")

guesses = ''

#any number of turns here
turns = 12

while turns > 0:

#counts numbers of fails

    failed = 0

#all characters from the input word taking one at a time
    for char in word:

    #comparing that character with the charcter in guess
     if char in guesses:
        print(char, end=" ")

     else:
        print("_")

        #for every 1 will be counted in failure 
        failed += 1
    
    if failed == 0:
     #user wins if failure is 0 'you win' will print
        print("you win") 
    #this will print correct word
   
        print("the word is:", word)
    break
#if user inputs wrong alphabet will ask for new input
print()
guess = input("guess a character:")

# every character input will be stored in guesses
guesses += guess

#check input with charcters in the word
if guess not in word:

    turns -= 1
    #if the character doesnt match the word wrong will be output
    print("wrong")

# this will print number of turns left
    print("you have", + turns, 'more guesses')

    if turns == 0:
        print("you lose")
# website didnt finish the code, when i get better ill try to fix
        
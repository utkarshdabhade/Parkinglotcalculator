# Task 3(Advanced Level): Write a Python program to create a console-based Word-Solver Game

#Solution:


# First, we will import the library that we will be using to choose  
# any random words from a list of words  
import random as rdm  
  
# Here the user will be asked to enter their name first  
name1 = input("What is your NAME ? ")  
  
print("Best of Luck! ", name1)  
   
words1 = ['Donkey', 'Energy', 'Friend', 'Pretty',  
         'Python', 'Bottle', 'Mobile', 'Packet',  
         'Hockey', 'Pencil','Flight']  
   
# rdm.choice() function will choose one random word from the gven list of words  
word1 = rdm.choice(words1)    
print ("Please guess the characters: ")  
   
guesses1 = ''  
   
# we can use any number of turns here  
turns1 = 5  
   
   
while turns1 > 0:  
       
    # counting the number of times a user is failed to guess the right character  
    failed1 = 0  
       
    # all the characters from the input word will be taken one at a time.  
    for char in word1: 
        if char in words1:
            print(char, end=char) 
        else:  
            print("_")  
               
        # for every failure of the user 1 will be incremented in failed1  
        failed1 += 1  
               
   
    if failed1 == 0:  
        # user will win the game if failure is 0 and 'User Win' will be given as output  
        print("You won the round!")  
           
        # this will print the correct word  
        print("The word is: ", word1)  
        break  
       
    # if the user has input the wrong alphabet then  
    # it will ask user to enter another alphabet  
    guess1 = input("Guess another character:")  
       
    # every input character will be stored in guesses  
    guesses1 += guess1  
       
    # here, it will check input with the character in word  
    if guess1 not in word1:  
           
        turns1 -= 1  
           
        # if the input character doesnot match the word  
        # then "Wrong Guess" will be given as output  
        print("Incorrect")  
           
        # this will print the number of turns left for the user  
        print("You have ", + turns1, 'more guesses ')  
           
           
        if turns1 == 0:  
            print("Oops! You lost all your chances to guess the letters.!") 
            print ("The word is ", word1 )
            print("Never mind, Play smart..!") 


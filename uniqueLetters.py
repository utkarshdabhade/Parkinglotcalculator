# Task 2(Intermediate Level): Write a Python program to print all the unique characters in a given String 
# Problem Statement: 
# Write a program in Python to print the number of unique letters in a string. Only new letters from the string should be counted and not duplicates.
# Input : string1 = "India"
# Output : uniqueLetters = i,n,d,a
# Input : string1 = "Dedication"
# Output : uniqueLetters = d,e,i,c,a,t,o,n

# Solution :

string1 = "india"
unique_char1 = set(string1)
print ("List of unique characters are :")
print (unique_char1)

string2 = "dedication"
unique_char2 = set(string2)
print ("List of unique characters are :")
print (unique_char2)

string3 = input("Enter your desired word:")
unique_char3 = set(string3)
print ("List of unique characters are :")
print (unique_char3)



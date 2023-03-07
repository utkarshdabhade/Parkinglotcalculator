# Take two inputs from user
firstNumber= input("Enter first number :")
secondNumber = input ("Enter second number :")

#To check if inputs are numbers

try:
    val1 = int(firstNumber)
except ValueError:
   print('Please provide first input in numerical format!') 
 
   
try:
    val2 = int(secondNumber)
except ValueError:
   print('Please provide second input in numerical format!')  

# Formulaes

sumoftwonos = int(firstNumber) + int(secondNumber)
productoftwonos = int(firstNumber)*int(secondNumber)

#To check if inputs are even or odd numbers

if (int(firstNumber) % 2 == 0):
    print ('The first input is an even number')
else:
    print ('The first input is odd number')

if (int(secondNumber) % 2 == 0):
    print ('The second input is an even number')
else:
    print ('The second input is odd number')


# To print "Values not acceptable" if one input is even and other input is odd.

if (int(firstNumber) % 2 == 0) and (int(secondNumber) % 2 != 0):
    print (" Values not acceptable. You need to provide either both inputs in even numbers or odd numbers.")
elif ((int(firstNumber) % 2 != 0) and (int(secondNumber) % 2 == 0)):
    print (" Values not acceptable. You need to provide either both inputs in even numbers or odd numbers.")

 #To print product of two numbers if they are odd numbers and to print sum of two numbers if they are even numbers
elif (int(firstNumber) % 2 == 0) and (int(secondNumber) % 2 == 0):
     print ("The sum of two inputs is:",sumoftwonos)
else:  
     print ("The product of two inputs is:",productoftwonos)




#To check if numbers are prime numbers

if int(firstNumber) == 1:
    print ("The first input is not a prime number.")
elif int(firstNumber) > 1:
    for index in range(2, int(firstNumber)):
        if ((int(firstNumber) % index) == 0):
            print (firstNumber, "is not a prime number")
            break
    else:
        print (firstNumber, "is a prime number")
else:
    print (firstNumber, "is not a prime number")

if int(secondNumber) == 1:
    print ("The first input is not a prime number.")
elif int(secondNumber) > 1:
    for index in range(2, int(secondNumber)):
        if ((int(secondNumber) % index) == 0):
            print (secondNumber, "is not a prime number")
            break
    else:
        print (secondNumber, "is a prime number")
else:
    print (secondNumber, "is not a prime number")




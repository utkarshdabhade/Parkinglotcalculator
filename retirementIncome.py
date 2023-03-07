# Problem Statement: 
# Create a Python console-based application for Retirement Calculator. 
# The program should determine how many years the User has left until retirement and the year the User can retire. 



#Since we will enter date of birth we will import date.

from datetime import date

# We need to take user inputs as follows:

name = input ("Enter your name :")
def get_user_birthday():
    birth_year = int(input('Please enter your birth year: '))
    birth_month = int(input('Please enter your birth month: '))
    birth_day = int(input('Please enter your birth day: '))

    #Convert user input into datetime object
    user_birthday = date(birth_year, birth_month, birth_day)

    return user_birthday
annualIncome = input ("Enter you current annual income in Rs. ")
annualExpense = input ("Enter your current annual expense in Rs. ")
savingsRate = input ("Enter your current Savings rate in percentage")
currentPortfolio = input ("Enter your current portfolio value in Rs. ")

def calculate_age(user_birthday):
    #Get current date
    today = date.today()
    #Calculate the years difference
    year_diff = today.year - user_birthday.year
    #Check if birth month and birth day preced current month and current day
    precedes_flag = ((today.month, today.day) < (user_birthday.month, user_birthday.day))
    #Calculate the user's age
    age = year_diff - precedes_flag
    #Return the age value
    return age

if __name__ == "__main__":
    user_birthday = get_user_birthday()
    current_age = calculate_age(user_birthday)
    print(f"Your age is: {current_age}")

# We need to calculate how much years are remaining for retirement.
remaining_retirement_Age = 60.00 - current_age

# We now calculate annual savings which is present value of income.
presentValue = int(annualIncome) - int(annualExpense)  #yearly savings 
# Calculate monthly expense
monthlyExpenses = int(annualExpense) / 12
#Calculate monthly savings
monthlySaving = int(presentValue)/ 12
#rounding off
roundedNumber1 = round(monthlyExpenses, 2)
roundedNumber2 = round(monthlySaving, 2)

#Calculate future of value of income as per rate of interest
futureValue = int(presentValue) * (1 + (int(savingsRate)/100)) * int(remaining_retirement_Age)

#Calculate total portfolio value
totalPortfolio = int(currentPortfolio) + int(futureValue)
roundedNumber3 = round(futureValue, 2)

#Outputs :
print("Dear ", name, "You can retire in ", remaining_retirement_Age, "years.")
print("with a savings rate of : ", savingsRate, " %")
print ("Annual expenses in Rs. :", annualExpense)
print ("Annual savings in Rs. : ", presentValue)
print("Annual income obtained during retirement in Rs. :", futureValue)
print("The total portfolio value during retirement in Rs. :", totalPortfolio)
print ("The monthly expense shall be in Rs. ", roundedNumber1)
print ("The monthly savings shall be in Rs. ", roundedNumber2)



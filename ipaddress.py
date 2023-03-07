# Task 3(Advanced Level):  Write a Python Program
# Problem Statement: Write a program in Python to create and print a valid IP Address from the given String of numeric values.
# Sample Input 1 :  addressString = "19216801"
# Output:   IP Address = 192.168.0.1


#Solution : 
# You can transform it to list and insert dots in required positions, ensuring that value is string.

string1 = input("Enter the string :")
l1 = list(str(string1))

# Add dots in positions you need

l1.insert(3, '.')
l1.insert(7, '.')
l1.insert(9, '.')

# If this is well-defined pattern. You can generalize the insertion above.

# After insertion is done, join them back to the string:

num = "".join(l1)

for i in num:
    print(i, end="")

def isValidIP(num):
 
    # check number of periods
    if num.count('.')!= 3:
        return 'This is Valid Ip address'
 
    l = list(map(str, num.split('.')))
 
    # check range of each number between periods
    for ele in l:
        if int(ele) < 0 or int(ele) > 255 or (ele[0]=='0' and len(ele)!=1):
            return 'This is Invalid Ip address'
 
    return 'This is Valid Ip address'
  
# Output
print(isValidIP(num))



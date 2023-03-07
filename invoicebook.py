# Problem Statement: Create a command-line program in Python to Calculate the total invoice amount for the below purchases - 
# •	Book - Introduction to Python Programming: Rs 499.00
# •	Book - Python Libraries Cookbook: Rs. 855.00
# •	Book - Data Science in Python: Rs. 645.00

# Taxes and additional charges are described as details - 
# •	GST: 12%
# •	Delivery Charges: Rs. 250.00

#Solution program as follows:

#Book Details:
book1 = ["Introduction to Python Programming", 499.00]
book2 = ["Python Libraries Cookbook", 855.00]
book3 = ["Data Science in Python", 645.00]

print ("The books purchased by customer as :", "\n", book1, "\n", book2, "\n", book3)

#GST & Delivery Charges to include:
gst = 0.12*(book1[1] + book2[1] + book3[1])
deliveryCharge = 250.00

#Calculate Total invoice amount:
totalInvoiceamount = book1[1] + book2[1] + book3[1] + gst + deliveryCharge
print ("The total amount for books purchased is: ", totalInvoiceamount)


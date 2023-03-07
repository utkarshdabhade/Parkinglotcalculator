# Parking lot issue

#List created for bike name, entry and exit time, total no. of hours, indivisual bike payment and total payment.
ratePerHour = 20
totalPayement = 0

bikes=[]

for index in range(100):
    # Accepting data from User: 1 for entry, 2 for exit, 3 for End of day. 
    data = input("Press:\n 1.Entry \n 2.Exit \n 3.End of Day\n")

    # Checking given data is numeric or not, if yes it will accept all the data else ask to enter number.
    if data.isnumeric():
        entry = int(data)

        # If user entered 1 for entry, 
        # lets accept the value and increment the list by appending the accepted data.
        if entry == 1:
            bike={}
            bikeName1 = input("enter bike name :")
            entryTime = int(input("enter the entry time :"))
            bike["name"]=bikeName1
            bike["entryTimes"]=entryTime
            bikes.append(bike)           
            print(bikes)

        # If user entered 2 for exit, 
        # check if there are any bikes present or not,
        # if there are no bikes, informing user about same
        # if there are bikes, check if the bike present, if yes search the bike and calculate the single bike payment
        elif entry == 2:
            if len(bikes) == 0:
                print("No bikes available.")
            else:
                bikeName = input("Enter bike name :")
                for i in range(len(bikes)):
                    # print(bikeNames)
                    if bikes[i]["name"] == bikeName:
                        bikes[i]["exitTimes"] = int(input("Enter the exit time :"))
                        bikes[i]["totalHours"] = bikes[i]["exitTimes"] - bikes[i]["entryTimes"]
                        bikes[i]["bikePayment"] = bikes[i]["totalHours"] *ratePerHour
                        print(bikes[i]["name"], "has payment of ",
                              bikes[i]["bikePayment"])
                    # else:
                    #     print(bikes[i]["name"] + " is not available.")
                        
        # # If user entered 3 for EOD,
        # # It will check if length of single bike payment is zero,
        # #if yes, it will return No bikes available,
        # # If no, calculate the  total payment and find if anything missing.
        elif entry == 3:
            if len(bikes) == 0:
                print("No bikes available, hence no amount collected.")
            else:
                for i in range(len(bikes)):
                    totalPayement = totalPayement + bikes[i]["bikePayment"]
                print("Total Payment: ", totalPayement)

                if totalPayement==0:
                    print("No bikes Exited.")
                else:
                    cashInHand = input("enter the cash in hand :")
                    if cashInHand == totalPayement:
                        print("Audit is successfully completed .")
                        break
                    else:
                        difference = int(totalPayement)-int(cashInHand)
                        print("The amount missing is ", difference)
                        break
                 
            
        else:
            print("Please enter either 1, 2 or 3.")

    else:
        print("Please enter number value")

#PROG 1700 – Tech Check #1
#Variables, Operators, Input/Output & Casting

#Student Name:    Andrew Beaver
#Program Title:  Restaurant Bill
#Description: Tech Check 1   

# Restaurant Bill 
# You will create a console-based Python program that will calculate the amount of the tip, the tax, and the 
# total amount of a restaurant bill. The program will prompt the user to input the original amount of the bill. 
# The program will then output the amount of the tax (15% of the original amount) and a tip (20% of the original amount). 
# Finally, the program will output the new total of the bill.


def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    #Welcome User to the program
    print("Hello, welcome to the Bill Total calculator. We will calculate the total price with the tax and tip.")
    #Prompt user to enter th eprice
    billPrice = float(input("\nPlease enter the price of the original bill: "))

    #Do math to calculate the tax and tip
    billTax = billPrice * 0.15
    billTip = billPrice * 0.20
    totalPrice = billPrice + billTax + billTip

    #display tax
    print("Your tax is: ${0:,.2f}".format(billTax))
    
    #display tip
    print("Your tip is: ${0:,.2f}".format(billTip))

    #display total
    print("Your total is: ${0:,.2f}".format(totalPrice))



    # YOUR CODE ENDS HERE

main()
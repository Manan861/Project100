class atm:
    def __init__(self, cardNumber, PIN):
        self.cardNumber=cardNumber
        self.PIN=PIN
    
    def checkBalance(self):
        print("Your balance is 56000")

    def withdraw(self,amount):
        newAmount=56000-amount
        print("You have withdrawn amount " + str(amount)+ " Your remaining balance is " +str(newAmount))

def main():
    card_Number=input("Enter your card number: ")
    pin_no=input("Enter your PIN number: ")
    new_user=atm(card_Number, pin_no)
    print("Choose your activity")
    print("1. Balance inquiry                    2. Withdraw")
    activity=int(input("Enter activity number: "))
    if (activity==1):
        new_user.checkBalance()
    elif(activity==2):
        amount=int(input("enter amount to withdraw: "))
        new_user.withdraw(amount)
    else:
        print("Please enter a valid number")
    

if __name__=="__main__":
    main()


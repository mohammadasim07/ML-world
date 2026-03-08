class Atm:
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.manu()


 
    def manu(self):
        user_input = input("""
        Hi how can I help you?
        1. Press 1 to create pin
        2. Press 2 to change pin
        3. Press 3 to check balance
        4. Press 4 to withdraw
        5. Anything else to exit
        """)

        if user_input == '1':
        #create pin
            self.create_pin()
        elif user_input == '2':
        #create pin
            self.change_pin()
            pass
        elif user_input == '3':
        #create balance
            self.check_balance()
            pass
        elif user_input == '4':
        #withdraw
            self.withdraw()
            pass
        else:
            exit()



    def create_pin(self):
        user_pin = input('enter your pin')   
        self.pin = user_pin

        user_balance = int(input('enter balance'))
        self.balance = user_balance

        print('pin created successfully')
        self.manu()
    


    def change_pin(self):
        old_pin = input('enter your old pin')
        
        if(old_pin == self.pin):
           new_pin = input("Enter new pin") 
           self.pin = new_pin
           print('pin changed successfully')
           self.manu()
        else:
            print("Wrong pin")
            self.manu()



    def check_balance(self):
        user_pin = input('enter your pin')
        if user_pin == self.pin:
            print('your balance is ',self.balance)
        else:
            print('pin is wrong')
        self.manu()



    def withdraw(self):
        user_pin = input('enter your pin')
        if user_pin == self.pin:
            amount = int(input("Enter amount"))
            if amount <= self.balance:
                self.balance -= amount
                print("amount withdrawal ",amount," now balance = ",self.balance )
            else:
                print("amount is not sufficient")
            self.manu()
        else:
            print("pin is wrong")




obj = Atm()
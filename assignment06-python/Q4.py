#4. Class Variables and Class Methods
#Assignment:
#Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "UBL Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display(self):
        print(f"Bank name: {Bank.bank_name}")


bank = Bank()
bank.display()

Bank.change_bank_name("MEEZAN Bank")

bank.display()
class BankAccount:
  Accounts = {}
  def __init__(self, number, balance):
    self.__number = number
    self.__balance = balance
    
    print(f"You're Account Number is: {self.__number} and You're Account Balance is: {self.__balance} $")
  
  def deposit(self, cash):
    self.__balance += cash
    
    print(f"You have made a deposit of {cash}$ to Your account {self.__number}")
    print(f"You're account balance increased to  {self.__balance} $")
  
  def withdraw(self, cash):
    if self.__balance >= cash:
     self.__balance -= cash
     print(f"You have withdrawn {cash}$")
    else:
     print(f"You don't have Enough money to withdraw")
     
  def check_balance(self):
    return self.__balance
  
  def check_account_number(self):
    return self.__number
  
my_bank_account = BankAccount(1234, 2000)
my_bank_account.deposit(1000)
my_bank_account.check_balance
my_bank_account.withdraw(4000)
my_bank_account.withdraw(1000)

Accounts = {}
Accounts[my_bank_account.check_account_number()] = my_bank_account
print(Accounts)

while True:
  print("1. Create Account \n2. Deposit \n3. Withdraw \n4. Check Balance \n5. Exit")
  option = input("Choose an option: ")
  if option.strip() == "1":
    number = int(input("Enter your new account number: "))
    balance = float(input("Enter your initial balance, the least amount is 50$"))
    while balance < +50:
      print("invalid amount!")
      balance = float(input("Enter your initial balance, the least amount is 50$ and can't be nagative value"))
    else: 
      #create account: 
      account = BankAccount(number, balance)
      #add the account to accounts Dictionary: 
      Accounts[account.check_account_number()] = account
      print(Accounts)
      
    
  elif option.strip() == "2":
    number = int(input("Enter your account number: "))
    if number not in Accounts.keys():
      print(f"Could'nt find the account {number}")
    else:
      print(f"Account Found with number {number}")
      cash = float(input("Enter your deposit amount: "))
      if cash  > +10:
        Accounts[number].deposit(cash)
      else: print("invalid cash amount")
      
  elif option.strip() == "3":
    account = int(input("Enter your account number: "))
    if account not in Accounts.keys():
      print(f"Could'nt find the account {account}")
    else: 
      cash = float(input("Enter your withdrawal amount: "))
      Accounts[account].withdraw(cash)
      
      
  elif option.strip() == "4":
    number = int(input("Enter your new account number: "))
    if number not in Accounts.keys():
      print(f"Could'nt find the account {number}")
    else:
      print(Accounts[number].check_balance())
    
  elif option.strip() == "5":
    print("Exiting the program...")
    break
  else: print("Wrong option, please retry!")

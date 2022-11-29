menu = """

[d] Deposit
[w] Withdrawals
[e] Extract
[x] Exit

==> """

balance = 0
limit = 10000
extract = ""
number_of_withdrawals = 0
WITHDRAWALS_LIMIT = 10

while True:
  
    option = input(menu)
    
    if option == "d":
        value = float(input("Enter the deposit amount: "))
        
        if value > 0:
          balance += value
          extract += f"Deposit: R$ {value:.2f}\n"
          
        else:
          print("Operation error! The value is invalid.")
    
    elif option == "w":
        value = float(input("Enter the withdrawals amount: "))
        
        surplus_amount = value > balance
        
        surplus_limit = value > limit
        
        surplus_withdrawals = number_of_withdrawals >= WITHDRAWALS_LIMIT
        
        if surplus_amount:
          print("Operation error! You don't have enough balance.")
          
        if surplus_limit:
          print("Operation error! The withdrawals exceeds the limit.")
          
        if surplus_withdrawals:
          print("Operation error! The withdrawals' limit has been exceeded.")
          
        elif value > 0:
            balance -= value
            extract += f"Withdrawals: R$ {value:.2f}\n"
            number_of_withdrawals += 1
            
        else:
            print("Operation error! The entered value is invalid")
            
    elif option == "e":
      print("\n=============================== EXTRACT ===============================")
      print("No enterings were made." if not extract else extract)
      print(f"\nBalance: R${value:.2f}")
      print("=========================================================================")
      
    elif option == "x":
        break
      
    else:
      print("Invalid operation, please select a new desired operation")

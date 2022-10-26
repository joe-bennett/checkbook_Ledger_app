import os
#Checks to see if a Ledger currently exists in local directory, if not it creates one.
#Ledger begins with two '0' values in order to provide functionality to the functions that use [-2] list location to find previous bal
if os.path.exists('Ledger.txt')==False:
    with open('Ledger.txt','w') as f:
        f.writelines(['0\n','0\n'])

#Pulls the last line of the ledger, which is the current balance
def get_current_bal():
    with open('Ledger.txt','r') as f:
        current_bal= f.readlines()
    return current_bal[-1] 
#Creates a main menu and promps user to make a selection on what action they wish to take
def main_menu():
    print(""" 
    
    ~~~ Welcome to your terminal checkbook! ~~~

    What would you like to do?

    1) view current balance
    2) record a debit (withdraw)
    3) record a credit (deposit)
    4) exit


                """)

    choice= input('Your choice?')

    if choice == '4':
        exit()
    if choice == '3':
        credit_deposit()
    if choice == '2':
        debit_withdrawl()
    if choice == '1':
        print(get_current_bal())
        main_menu()


 #Function is only called if a transaction is made. It displays the previous balance prior to the transaction   
def get_previous_bal():
    with open('Ledger.txt','r') as f:
        previous_bal= f.readlines()
    return previous_bal[-2] 

#Asks how much the deposit is for, then adds the deposit to the current balance. promps user to input yes to return to main menu
def credit_deposit():
    deposit=input('How much is your deposit?')
    deposit=float(deposit)
    with open('Ledger.txt','a') as f:
        f.writelines(str(float(get_current_bal()) + deposit)+'\n')
    print(f""" Previous bal:{get_previous_bal()}

             Deposit amount:{deposit}


                New balance:{get_current_bal()}
    
    
    """)

    return_to_main=input('Type yes to return to main menu')
    if return_to_main == 'yes':
        return main_menu()
        


def debit_withdrawl():
    withdrawl=input('How much is your withdrawl?')
    withdrawl=float(withdrawl)
    with open('Ledger.txt','a') as f:
        f.writelines(str(float(get_current_bal()) - withdrawl)+'\n')
    print(f""" Previous bal:{get_previous_bal()}

             Withdrawl amount:{withdrawl}


                New balance:{get_current_bal()}
    
    
    """)

    return_to_main=input('Type yes to return to main menu')
    if return_to_main == 'yes':
        return main_menu()

main_menu()




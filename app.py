#operations
operations=(
    "1.Balance \n"
    "2.Withdraw\n "
    "3.Deposit \n"
    "4.Transfer \n"
    "5.Histroy \n"
    "6.Logout"
)
#accounts_table
accounts= {12345 : '6789',
           12346 :'7777'} #this is dict and key value pair
#usertbale details
user_Details= {
    12345:["usha",1000,"ushabitra1299@gmail.com"],
    12346:["mahi",20000,"mahib123@gamil.com"]
}
#logic function
def login(user_name:int,password:str):
    if user_name in accounts:
    #checking whether the password in account 
        if accounts[user_name]==password:
            print("Succesfully Login to online Banking Platform")#if cond true login
            return True
        else:
            print("Wrong Password")
    else:
        print("Invalid Username")
    return False
   
    pass
#opertions function creation
#balance function creation
def balance(user_name:int):
    if user_name in user_Details:
        amount=user_Details[user_name]
        print(f"current balance is: {user_Details[user_name][1]}")

    #user not present in the usertable
    else:
        print("user not found")
    #pass #used to overcome the error
#withdraw function creation
def withdraw(user_name:int,withdraw_amount):
   #chekc whther the user in the usertable
    if user_name in user_Details:
        amount=user_Details[user_name][1]
        if withdraw_amount<=amount:
          user_Details[user_name][1]-=withdraw_amount
          print(f"Successfully withdraw your amount{withdraw}")
          print(f"current balnace is:{user_Details[user_name][1]}")
        else:
            print("Insufficient amount in account")

    #user not present in the usertable
    else:
        print("user not found")
    
    pass
#deposit function creation
def deposit(user_name:int,deposit_amount:int):
    if user_name in user_Details:
        user_Details[user_name][1] += deposit_amount
 #here we are adding the amunt+deposite
        print(f"current balnace is:{user_Details[user_name][1]}")

    #user not present in the usertable
    else:
        print("user not found")

    pass
#transfer funciton creation
def transfer(user_name:int,to_account:int,transfer_amount:int):
    if user_name in user_Details:
        if to_account in user_Details:
            amount=user_Details[user_name][1]
            if transfer_amount<=amount:
                user_Details[user_name][1]-=transfer_amount
                user_Details[to_account][1]+=transfer_amount
                print(f"current balnace is:{user_Details[user_name][1]}")
            else:
                print("Insufficient amount in account")
        else:
            print(f"{to_account} user not found")

    #user not present in the usertable
    else:
        print(f"{user_name} user not found")
    #user not present in the usertable
    
   
    pass
#mini statement function 
def history(user_name:int):
    print("DEVELOPMENT ON PROCESS")
    pass
#creation of logout fucniton
def logout():
    print("User succesfully logout")
    exit() #exit used for exiting the application.
    pass
#main function
if __name__=="__main__":
    print("Welcome to online Net Banking Platform")
    user_account = int(input("Enter Your Account Number: "))  
    password = input("Enter Your Password: ")
    if login(user_name=user_account, password=password):
        while True:
            print(*operations)
            choice=int(input("please select operation: "))
            
            if choice==1:
                balance(user_name=user_account)
            elif choice==2:
                amount=int(input("please enter the amount for withdraw: "))
                withdraw(user_name=user_account, withdraw_amount=amount)
            elif choice==3:
                amount=int(input("please enter the amount for Deposit: "))
                deposit(user_name=user_account, deposit_amount=amount)
            elif choice==4:
                reciver_acc=int(input("please enter your receiver amount number:"))
                amount=int(input("please enter the amount for transfer: "))
                transfer(user_name=user_account, to_account=reciver_acc, transfer_amount=amount)
            elif choice==5:
                history(user_name=user_account)
            elif choice==6:
                logout()
            else:
                print("Please enter between 1 to 6")

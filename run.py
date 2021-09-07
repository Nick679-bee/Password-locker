from user import User
from credentials import Credentials


"""This is the file that runs the application
Import User Class from User Module and Credential Class from Credential Module"""

def create_new_user(username,password):
    '''
    Function to create a new user with a username and password
    '''
    new_user = User(username,password)
    return new_user



def save_users(user):

    """"
    Function to save a user account
   """
    
    user.save_user()


  
def display_user():
    """
    Function to display existing user
    """
    return User.display_user()



def login_user(name,password):
    """
    Function that allows a user to log into their credential account
    """
  
    check_user = Credentials.verify_user(name,password)
    return check_user



def create_credentail(account,username, password):
    '''
    Function to create a credential 
    '''

    new_credentail = Credentials(account,username,password)

    return new_credentail

def save_details(Credentials):
    '''
    Function to save a credential
    '''

    Credentials.save_de()



def check_existing_credentials(account):
    '''
    Function that checks if a user credential name already exists

    '''

    return Credentials.find_credential(account)



def display_accounts_details():
    """
    Function that returns all the saved credential.
    """
    return Credentials.display_credentials()



def delete_credential(credentials):
    """
    Function to delete a Credentials from credentials list
    """
    credentials.delete_credentials()



def find_credential(account):
    """
    Function that finds a Credentials by an account name and returns the Credentials that belong to that account
    """
    return Credentials.find_credential(account)



def create_generated_password():
    '''
    Function that generates a password for the user 
    ''' 
    password = Credentials.generate_password()

    return password



def main():
    '''
    Function running the PasswordLocker app
    '''

    print("""Welcome to Password Locker \n
            Use these short codes to navigate""")
    go = True
    while go:
        print("""  Short codes:
        ca- create a Password Locker account \n
        li - already have an account \n""")

    
        short_code=input("").lower().strip()
    
        if short_code == "ca":
        
            print("Sign Up")
        
            print('*' * 50)
            username = input("User_name: ")

            print(" cp - To type your own pasword:\n gr - To generate random Password")
            password_Choice = input().lower().strip()
            if password_Choice == 'cp':
                password = input("Enter Password\n")
                
            elif password_Choice == 'gr':
                password = create_generated_password()
                
            else:
                print("Invalid command")
                

            save_users(create_new_user(username,password))

            print("\n")
            print(f"Hello {username}, welcome to PasswordLocker! Your password is: {password}")
            print('please remember your password')
            print("\n")
            
        elif short_code == "li":

            print("*"*50)
            print("Enter your User name and your Password to log in:")
            print('*' * 10)

            username = input("User_name: ")
            password = input("password: ")

            login = login_user(username,password)

            if login_user == login:
                print('\n')
                print(f"Hello {username}.Welcome To PasswordLocker.")  
                print('\n')

            
            while True:
                print(""" use this Short codes:
                    nc- create a new credential \n
                    dc - Display Credentials \n 
                    fc - Find a credential \n
                    de - Delete credential \n 
                    ex - Exit the application """)
        
                short_code = input().lower().strip()
                if short_code == "nc":
                    print("Create New Credential")
                    print("."*20)
                    print("Account name ....")
                    account = input().lower()
                    print("Your Account username")
                    username = input()

                    while True:
                        print(" cp - To type your own password :\n gr - To generate random Password")
                        password_Choice = input().lower().strip()
                        if password_Choice == 'cp':
                            password = input("Enter Your Own Password\n")
                            break
                        elif password_Choice == 'gr':
                            password = create_generated_password()
                            break
                        else:
                            print("Invalid command")


                    save_details(create_credentail(account,username,password))

                    print('\n')
                    print(f"Account Credential for: {account} has been created succesfully")
                    print('\n')


                elif short_code == "dc":

                    '''
                    Displaying credential name and password
                    '''

                    if display_accounts_details():
                            print('*' * 30)
                            print("This is your list of accounts saved: ")
                            print('*' * 30)

                            for account in display_accounts_details():
                                print('*' * 40)
                                print(f" Account:{account.account} \n Username:{username}\n Password:{password}")
                                print('_'* 40)
                    else:
                            print("You don't have any credentials saved yet..........")

                elif short_code == "fc":
                        print("Enter the Account Name you want to search for")
                        search_name = input().lower()

                        if find_credential(search_name):
                            search_credential = find_credential(search_name)
                            print(f"Account Name : {search_credential.account}")
                            print('-' * 40)
                            print(f"User Name: {search_credential.userName} Password :{search_credential.password}")
                            print('-' * 40)

                        else:
                            print("Unexisting credential")
                            print('\n')

                elif short_code == "de":

                        print("Enter the account name of the Credentials you want to delete")

                        search_name = input().lower()

                        if find_credential(search_name):
                            search_credential = find_credential(search_name)

                            print("_"*50)
                            search_credential.delete_credentials()
                            print('\n')
                            print(f"Your stored credentials for : {search_credential.account} successfully deleted!!!")
                            print('\n')

                        else:
                            print("That Credential you want to delete does not exist in your store yet")

                
                elif short_code == 'ex':
                        '''
                        Exit Password Locker
                        '''
                        print("\n")
                        print("Bye .you are always welcomed here")
                        go =  False
                                    
                        break

                    
                else :

                    login_user(username,password) == None
                    print("\n")
                    print("Please try again or create an account")
                    print("\n")
            
 
        else:
            print("\n")
            print(f'''Cannot find  {short_code}?
            Please use the short codes''')
            print("\n")

if __name__ == '__main__':
    main()

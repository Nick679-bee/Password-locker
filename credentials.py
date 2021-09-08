import random
import string
from user import User

"""
Import random and string modules from Python for generating passwords
"""

#class credentials#

class Credentials():
    """
    Create credentials class to help create new objects of credentials
    """

    credentials_list = [] #empty credetial lists#

    def __init__(self,account,username, password):
        """
        method that defines user credentials to be stored
        """
        self.account = account
        self.username = username
        self.password = password

#save credentials#

    def save_details(self):
        """
        method to store a new credential to the credentials list
        """
        Credentials.credentials_list.append(self)

#delete credentials#

    def delete_credentials(self):
        """
        delete_credentials method that deletes an account credentials from the credentials_list
        """
        Credentials.credentials_list.remove(self)

#look for credentials#

    def find_credential(cls, account): 
        """
        Method that takes in a account_name and returns a credential that matches that account_name.
        """
        for credential in cls.credentials_list:
            if credential.account == account:
                return credential

#check credentials#

    @classmethod
    def if_credential_exist(cls, account):
        """
        confirm a class exists
        """
        for credential in cls.credentials_list:
            if credential.account == account:
                return True
        return False

#display credentials#

    @classmethod
    def display_credentials(cls):
        '''
        method that returns all credentials
        '''
        return cls.credentials_list

#generate password#

    @classmethod
    def generate_password(cls):
        '''
        Method that generates a random alphanumeric password
        '''
        # Length of the generated password
        size = 8

        # Generate random alphanumeric 
        alphanum = string.ascii_uppercase + string.digits + string.ascii_lowercase

        # Create password
        password = ''.join( random.choice(alphanum) for i in range(size) )
        
        return password

#verify user#

    @classmethod
    def verify_user(cls,username, password):
        """
        method to verify whether the user is in our user_list or not
        """
        a_user = ""
        for user in User.user_list:
            if(user.username == username and user.password == password):
                    a_user == user.username
        return a_user

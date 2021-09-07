#class user#

class User:
    '''
    Class that generates new instances of user
    '''
    user_list = []  # empty users list

    def __init__(self, username, password):
        '''
        method defines properties for our objects in User.
        '''
        self.username = username
        self.password = password

#save user#

    def save_user(self):
        """
        a method that saves User objects into user_list
        """
        User.user_list.append(self)

#delete user#

    def delete_user(self):
        '''
        deletes a saved contact from the user_list
        '''
        User.user_list.remove(self)

#Display#

    @classmethod
    def display_user(cls):
        '''
        Method that returns the user list
        '''
        
        return cls.user_list

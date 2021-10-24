class User():

    user_list = []

    def __init__(self, username, password):
        '''
        Function to initialize the user.
        '''
        self.username = username
        self.password = password

    def save_user(self):
        '''
        Function to save user to the list.
        '''
        User.user_list.append(self)

    def delete_user(self):
        '''
        Function to delete user from the list.
        '''
        User.user_list.remove(self)

    # @classmethod
    # def find_user(self):
    #     '''
    #     function to check whether the user account exists in the user accounts list.
    #     '''
    #     self.find_user = User.find_user('ezekiel')

    # def find_user_exist(self):
    #     '''
    #     Function to check if the user's account exists in the user accounts list.
    #     '''
    #     self.find_user_exist = User.user_exist('kezekiel')

    @classmethod
    def find_user(cls, username):
          '''
          function to check whether the user account exists in the user accounts list.
          '''
          for user in cls.user_list:
              if user.username == username:
                return user

    @classmethod
    def user_exist(cls, username):
          '''
           Function to check if the user's account exists in the user accounts list.
          '''
   
          for user in cls.user_list:
               if user.username == username:
                   return True
          return False

    @classmethod
    def check_user(cls, username, password):
          '''
          Function to check if the user's account exists in the user accounts list.
          '''
          user = cls.find_user(username)
          if user and user.password == password:
              return True
          return False
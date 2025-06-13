class UserTest:
    def __init__(self, username, password):
        self._username = username
        self.__password = password

    def get_credentials(self):
        return (self._username,self.__password)


user = UserTest("sunita","Sunita@1234")
print(user.get_credentials())


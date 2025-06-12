class LoginPage:
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def login(self):
        if self.username=="Admin" and self.password=="1234":
            print("login successful")
        else:
            print("Login Failed")

user1 = LoginPage("Admin","1234")
user1.login()
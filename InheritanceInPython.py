class BaseTest:
    def setup(self):
        print("this is basic setup")
    def tearDown(self):
        print("this is teardown method")

class loginUser(BaseTest):
    def AdminLogin(self):
        print("The user is logged in")

user1 = loginUser()
user1.setup()
user1.AdminLogin()
user1.tearDown()
class BaseTest:
    def run_test(self):
        print("this is first run test method")

class loginTest(BaseTest):
    def run_test(self):
        print("this is login test")

class logoutTest(BaseTest):
    def run_test(self):
        print("This is logout test")

basetest = BaseTest()
login = loginTest()
logout = logoutTest()

basetest.run_test()
login.run_test()
logout.run_test()
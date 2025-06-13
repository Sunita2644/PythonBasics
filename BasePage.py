class BasePage:
    def __init__(self,pagename):
        self.pagename = pagename
    def click(self,element):
        print("click on element",element)
    def type(self,value):
        print("enter value in element",value)


class LoginPage(BasePage):
    def __init__(self):
        super().__init__("login")

    def EnterUsername(self,value):
        self.type("username")
    def EnterPassword(self,value):
        self.type("password")
    def clickButton(self,element):
        self.click(element)


class loginTest(LoginPage):
    def run_test(self):
        loginPage1 = LoginPage()
        loginPage1.EnterUsername("sunita")
        loginPage1.EnterPassword("sunita")
        loginPage1.clickButton("submit")

test1 = loginTest()
test1.run_test()
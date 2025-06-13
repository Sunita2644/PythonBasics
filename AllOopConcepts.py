
class BrowserDriver:
    def launch(self):
        print("launched Browser")
    def quit(self):
        print("quiting browser")

class BaseTest:
    def __init__(self):
        self.driver = BrowserDriver()
    def setUp(self):
        self.driver.launch()
    def tearDown(self):
        self.driver.quit()

class Login(BaseTest):
    def run_test(self):
        print("running login test")
class Logout(BaseTest):
    def run_test(self):
        print("running logout test")

user1 = Login()
user2 = Logout()

ObjectsList = [user1,user2]
for object in ObjectsList:
    object.setUp()
    object.run_test()
    object.tearDown()
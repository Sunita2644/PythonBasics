from abc import ABC,abstractmethod
class AutomationScript(ABC):
    @abstractmethod
    def execute(self):
        pass

class SignUpScript(AutomationScript):

    def execute(self):
        print("Signup test running")
class SearchScript(AutomationScript):
    def execute(self):
        print("Search Test is running")

signup = SignUpScript()
signup.execute()

searchScript = SearchScript()
searchScript.execute()
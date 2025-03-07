class BaseClass:
    def __init__(self):
        self._protected_variable = 'Protected'
        self.__private_variable = "Private"

    def _protected_method(self):
        print("This is a protected method.")

    def __private_method(self):
        print("This is a private method.")

    def public_method(self):
        self.__private_method()
        
    
base = BaseClass()
# print(base._protected_variable)
# base._protected_method
base.public_method()
base.__private_method()
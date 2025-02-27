class User:

    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname

    def sayFirstName(self):
        print("меня зовут ", self.first_name)

    def sayLastName(self):
        print("Моя фамилия ", self.last_name)

    def sayFL(self):
        print(self.first_name, self.last_name)

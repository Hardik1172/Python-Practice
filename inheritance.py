# this is example of multiple inheritance
class name:
    name = "Ayush"
    def showname(self):
        print(f"the name of student is {self.name}")
class langugage:
    language = "Python"
    def showlanguage(self):
        print(f"he is best in {self.language}")
class company(name,langugage):
    company = "Nxp"
    def showcompany(self):
        print(f"{self.name} is selected due to {self.language} in {self.company}")
a = name()
b = langugage()
c = company()
c.showname()
c.showlanguage()
c.showcompany()
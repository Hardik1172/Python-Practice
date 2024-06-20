# super() keyword

class programmer():
    def __init__(self):
        print("Constructor of programmer")
        b = 2
class Mananger(programmer):
    def __init__(self):
        print("Contructor of manager")
        super().__init__()
        c = 3
a = Mananger()
 

import random
import string


def generate(self):
    self.randomletter = random.randrange(string.ascii_uppercase)
    self.randomid = random.randrange(1, 50)
    print(f"the passenger id is {self.randomletter}{self.randomid}")






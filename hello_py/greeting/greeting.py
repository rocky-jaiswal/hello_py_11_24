import os


class Greeting:
    def get_greeting(self):
        return "Hello Python!"

    def hello(self):
        print(self.get_greeting())


def hello():
    Greeting().hello()
    print("This script is in - " + os.getcwd())

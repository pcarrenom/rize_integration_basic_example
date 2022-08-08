import time

class Robot():

    def __init__(self, name):
        self.name = name

    def say(self, value, parameters):
        print("Hello, I'm saying something")
        print("Value", value, "Parameters", parameters)
        time.sleep(2)
        return "success"

    def move(self, value, parameters):
        print("Hello, I'm moving")
        print("Value", value, "Parameters", parameters)
        time.sleep(2)
        return "success"
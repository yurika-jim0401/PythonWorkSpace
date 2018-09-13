class Student():
    def __init__(self,name="NoName"):
        self.name = name

    def say(self):
        print("i am {0}".format(self.name))
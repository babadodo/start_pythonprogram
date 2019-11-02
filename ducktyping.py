class Pycharm:

    def execute(self):
        print("Typing")
        print("running")


class Myediter:
    def execute(self):
        print("Call")
        print("Call2")
        print("Call3")
        print("Call4")




class Laptop:

    def code(self,ide):
        ide.execute()

ide = Myediter()                                  #Duck Typing

a1 = Laptop()
a1.code(ide)
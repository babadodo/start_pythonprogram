

class A:

    def show(self):
        print("A is my")

class B(A):                     # this place create overriding
    def show(self):
        print("B is my")



a = B()
a.show()
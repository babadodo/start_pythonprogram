class Student:                             #outer_class

    def __init__(self,name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()



    def show(self):
        print(self.name, self.rollno)
        self.lap.show()


    class Laptop:                              #inner_class

        def __init__(self):
            self.brand = "HP"
            self.cpu = "i7"
            self.ram = 8


        def show(self):
            print(self.brand, self.cpu, self.ram)




s1 = Student("sajan",89)
s2 = Student("pawan",56)

s2.show()
s1.show()




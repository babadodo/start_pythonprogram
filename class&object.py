class computer:           #create class
    def config(self):         #create method
        print("I am Hero.")

    def config2(self):
        print("I am Villen.")


com1 = computer()               #create object for class
com2 = computer()

computer.config(com1)
computer.config2(com1)

com1.config()                    #using object
com2.config2()
class computer:

    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config is:", self.cpu, self.ram)



com1 = computer(5, 'Octa')
com2 = computer(7, 'duo')

com1.config()
com2.config()
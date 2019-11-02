class car:

    wheel = 4  #class or static variable and class namesapce


    def __init__(self):
        self.mil = 10   #instance namespace and instance vareable
        self.com = "BMW"


c1 = car()
c2 = car()
c1.mil = 20

print(c1.mil , c1.com, c1.wheel)
print(c2.com , c2.mil, c2.wheel)
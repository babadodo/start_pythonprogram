class student:

    school = "Lucknow Public"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3


    def avg(self):                                      #instancemethod
        return (self.m1 + self.m2 + self.m3)/3

    @classmethod
    def getschool(cls):
        return cls.school


    @staticmethod
    def info():
        print("This is the best...")


s1 = student(12,15,12)
s2 = student(25,26,23)


print(s1.avg())
print(s2.avg())
print(student.getschool())
student.info()
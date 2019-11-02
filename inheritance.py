class A:                         #super_class or Parent_class
    def feature1(self):
        print("1 is working")
    def feature2(self):
        print("2 is working")

class B(A):                         #child or base class            #single_level_inheritanc
    def feature3(self):
        print("3 is working")
    def feature4(self):
        print("4 is working")

class C(B):                                    #multilevel_inheritanc
    def feature5(self):
        print("5 is working")

class E:
    def feature7(self):
        print("7 is working")



class D(A,E):                                   #multiple_inheritance
    def feature6(self):
        print("6 is working")



a1 = A()

a1.feature1()
a1.feature2()

b1 = B()
b1.feature1()
b1.feature2()

c1 = C()
c1.feature2()

d1 = D()
d1.feature1()
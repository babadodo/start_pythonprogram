class A:
    def __init__(self):                          #constructer
        print("This is A constructer")

    def feature1(self):
        print("feature 1 is working")


class B:
    def __init__(self):
        super().__init__()                      #using super use parent constructer
        print("this is B construter")

    def feature2(self):
        print("2 is working")

class C(A,B):
    def __init__(self):
        super().__init__()                     # MRO(Method Resolutin Order) in this multiple inheritance firstly use left side class like class A
        print("C Constructer")


    def feat(self):
        super().feature1()


a1 = C()
a1.feat()
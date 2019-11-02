

f = open("school 2.PNG","rb")     #rb means read binary

f1 = open('Mypic.png','wb')

for i in f:
    f1.write(i)
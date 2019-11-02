

r = open('Mydata','r')

#print(r.readline(), end="")            read the data
#print(r.readline())

f1 = open('newdata','a')                   #usning w change all file  using a modify the data
f1.write(" is best")


for data in r:                           #copy data mydatafile to new data
    f1.write(data)

pos = -1
def search(list ,n):
    i = 0

    while i<len(list):
        if list[i] ==n:
            globals()['pos'] = i
            return True
        i = i+1
    return False


list = [2,5,9,6,3,8,]
n = 3

if search(list, n):
    print("found at",pos+1)
else:
    print("Not Found")
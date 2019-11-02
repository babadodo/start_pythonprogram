
import sys

sys.setrecursionlimit(10)

print(sys.getrecursionlimit())

i = 0

def recur():
    global i
    i = i + 1
    print("Hello", i)
    recur()

recur()

from functools import reduce


def is_even(n):
    return n%2==0

def is_double(n):
    return n*2

def is_sum(a,b):
    return a+b

nums = [2,6,5,4,9,7,3,1,5,]
even = list(filter(is_even,nums))
lambdaodd = list(filter(lambda n : n%2!=0 , nums))

double = list(map(is_double, even))
lambdadouble = list(map(lambda a : a*2, lambdaodd))

sum = reduce(is_sum,double)
lambdasum = reduce(lambda a,b : a+b , lambdadouble)

print(even)
print(lambdaodd)

print(double)
print(lambdadouble)

print(sum)
print(lambdasum)
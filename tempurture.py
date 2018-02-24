f=int(input("Enter a Tempurture===> "))


def f_to_c(f):
    
    return (f-32)*(5/9)


print(f_to_c(f))

def c_to_f(c):
    return c*(9/5)+32

print(c_to_f(f))
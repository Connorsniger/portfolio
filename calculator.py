

def add(num1,num2):
    return (num1+num2)


def subtract(num1,num2):
    return(num1-num2)



def Multiply(num1,num2):
    return(num1*num2)



def average(num1,num2):
    total=(num1+num2)
    return(total/2)



opp=input("what opperation do you want to do? ")
x=int(input("enter your first value===>  "))
y=int(input("enter your second value===> "))
if opp=="add":
    print(add(x,y))

elif opp=="subtract":
    print(subtract(x,y))


elif opp=="multiply":
    print(Multiply(x,y))


elif opp=="average":
    print(average(x,y))







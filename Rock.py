import random 
choice=(random.randint(1,3))

user=input("what do you want to do,1 rock,2 paper, or 3 scissors? ")


if choice==1 and user=="rock":
    print("you tied")
if choice==1 and user=="paper":
    print("you win")
if choice==1 and user=="scissors":
    print ("you lose")
if choice==2 and user=="rock":
    print("you lose")
if choice==2 and user=="paper" 
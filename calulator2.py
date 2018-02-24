list = [65, 25, 5, 10, 15, 20]

def add(list1):
   total=0
   for  i in range(len(list1)):
      total+=list1[i]
   
   return total

print(add(list)) 


def average(list1):
  
   return add(list1) / len(list1)

print(average(list))
      
      
      
      
      
      
      
def median(list1):
   
   list1.sort()
   return list1[len(list1)//2]
   
print(median(list))
   
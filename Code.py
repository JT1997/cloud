#Sum of even number from 1-10
def sum():
    s=0
   for i in range (1,11):
        if i%2==0: 
            s=i+s
    print(s)
sum()


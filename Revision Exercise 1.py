#Adam Howe
#Revision Exercise 1
#02/12/2014



def OutputSymbols(n,c):
    for counter in range(n):
        print(c,end="")



c = str(input("What characters do you want displayed: "))
n = int(input("How many of the character do you want displayed: "))
t = OutputSymbols(n,c) 

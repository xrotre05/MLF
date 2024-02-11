print("Exercise 1")
print("Exercise 1.1\n")


X01=1
i=1
while i >= 1:
    print(i*"X ")
    if (i<5)&(X01==1):
        i+=1
    else:
        i-=1
        X01=0

print("\nExercise 1.2\n")


input_str = "n45as29@#8ss6"
res=0
for x in input_str:
    try:
        res=res+int(x)
    except:
        res=res
print("Sum= "+str(res))

print("\nExercise 1.3\n")
import random
int_num=random.randrange(1,1000)
print("Random integer: "+str(int_num))
bin_num=int_num
bits=""

while (bin_num)>=1:
    if ((bin_num)%2)==1:
        bits="1"+bits
    else:
        bits="0"+bits
    bin_num=int(bin_num/2)

print("Conversion to bits: "+str(bits))

print("\nExercise 1.4\n")

def fibonaci(fib_num):
    f1=0
    f2=1
    fib_str=("["+str(f1)+", "+str(f2))
    
    while f2<fib_num:
        
        f_temp=f1+f2
        f1=f2
        f2=f_temp
        if f2>fib_num:
            break
        fib_str=fib_str+", "+str(f2)
 
    fib_str=fib_str+"]"
    return fib_str

fn=200
print("upper limit: "+str(fn))
print(fibonaci(fn))

print("\nExercise 1.5\n")

def rock_paper_scissors(rounds=3):
    i=0
    userscore=0
    pcscore=0
    while i< rounds:
        print("Round "+ str(i+1))
        RPS = input("Enter your move: ")
        strRPS=["rock","paper","scissors"]
        pcmove=random.randrange(1,4)-1
        print("pcmove: "+ str(strRPS[pcmove]))
        
        # user move
        if RPS.lower()== strRPS[0].lower(): # rock
            usermove=0
        elif RPS.lower()== strRPS[1].lower(): # paper
            usermove=1
        elif RPS.lower()== strRPS[2].lower(): # scissors
            usermove=2  
        else:
            print("invalid move")
            continue
                
        print("usermove: "+ str(strRPS[usermove]))

        # round result
        if (usermove-1==pcmove) or (usermove==pcmove-2):
            print("You win")
            userscore+=1
        elif (usermove==pcmove-1) or (usermove-2==pcmove):   
            print("You lose")
            pcscore +=1
        elif usermove==pcmove:
            print("It is a tie")

        print("Current score: "+str(userscore)+":"+str(pcscore))
        i+=1
    print("Final score: "+str(userscore)+":"+str(pcscore))

    if userscore>pcscore:
        print("You win")
    elif userscore<pcscore:
        print("You lose")
    elif userscore==pcscore:
        print("It is a tie")


#rock_paper_scissors()

print("\nExercise 2")
print("Exercise 2.1\n")

import numpy as np

#create rand 5x5 array
from numpy import random
x = random.randint(25, size=(5, 5))
print(x)

def arrless(ranarr,tresh):
    compare = ranarr > tresh
    #print(compare)
    print(ranarr*compare) 

tresh=13
arrless(x,tresh)    
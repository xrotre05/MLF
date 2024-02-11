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
print(res)

print("\nExercise 1.3\n")
import random
int_num=random.randrange(1,1000)
bin_num=int_num
bits=""

while (bin_num)>=1:
    if ((bin_num)%2)==1:
        bits="1"+bits
    else:
        bits="0"+bits
    bin_num=int(bin_num/2)

print(bits)

print("\nExercise 1.4\n")

def fibonaci(fib_num):
    f1=0
    f2=1
    fib_str=("["+str(f1)+", "+str(f2))
    
    while f2<fib_num:
        
        f_temp=f1+f2
        f1=f2
        f2=f_temp
        if f2<fib_num:
            break
        fib_str=fib_str+", "+str(f2)
 
    fib_str=fib_str+"]"
    return fib_str

print(fibonaci(10))

def flipbits(num1,num2):
    flips=0
    while (num1>0 or num2>0):
        t1=num1&1
        t2=num2&1
        if(t1!= t2):
           flips+=1
        num1>>=1
        num2>>=1
    return flips 
        
n1=int(input("ENTER FIRST NUMBER"))
n2=int(input("ENTER SECOND NUMBER"))
print("NO. OF FLIPS TO MAKE THE NUMBERS EQUAL IS ",flipbits(n1,n2))

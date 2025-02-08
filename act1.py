def powerset(set,setsize):
    powersetsize=2*setsize
    outer=0
    inner=0
    for outer in range(0,powersetsize):
        for inner in range(0,setsize):
            if((outer&(1<<inner))>0):
                print(set[inner],end=" ")
        print("")


size=int(input("enter size of array "))
set=[]

for i in range(0,size):
    n=int(input("enter element"))
    set.append(n)

 
powerset(set,len(set))

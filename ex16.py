a=int(input(""))
b=int(input(""))
for num in range(a,b+1):
    if(num>0):
        for i in range(2,num):
            if(num%i==0):
                break
        else:
            print(num)

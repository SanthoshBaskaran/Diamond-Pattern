size=int(input("Enter diamond size:"))
count=0
start=size//2
end=size//2
counter=0
for i in range(0,size):
    for j in range(0,size):
        if(count>=start and count<=end):
            print('*',end=" ")
        else:
            print(" ",end=" ")
        count=count+1
    counter=counter+1
    print()
    if(counter>=size//2):
        start=start+1
        end=end-1
    else:
        start=start-1
        end=end+1
    count=0

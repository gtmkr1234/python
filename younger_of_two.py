n1=str(input())
d1=input()
n2=str(input())
d2=input()
y1=(d1[6:10])    
y2=(d2[6:10])
mo1=(d1[3:5])    
mo2=(d2[3:5])
day1=(d1[0:2])   
day2=(d2[0:2])
if(y1>y2):
    print(n1)
elif(y1<y2):
    print(n2)
else:
    if(mo1>mo2):
        print(n1)
    elif(mo1<mo2):
        print(n2)
    else:
        if(day1>day2):
            print(n1)
        elif(day1<day2):
            print(n2)
        else:
            if(n1>n2==True):
                print(n2)
            else:
                print(n1)
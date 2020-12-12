max=int(input("Enter any number"));
number=0;
print("prime numbers between 0 and max are:\n");
while(number<=max):
    count=0;
    i=2;
    while(i<=number//2):
        if(number%i==0):
            count+=1;
            break;
        i+=1;
    if(count==0 and number!=1):
        print(number,end=' ');
    number=number+1
        
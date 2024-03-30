
#Prime_Number

#Procedural Approach

num=int(input("Enter A Number : "))
count=0
for factors in range (1,num+1):
    if num%factors==0:
        count+=1
if(count==2):
    print("Prime Number")
else:
    print(" Not A Prime Number")


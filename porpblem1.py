# Greatest number among four number entered by user
a = int(input("Enter the 1st number : "))
b = int(input("Enter the 2nd number : "))
c = int(input("Enter the 3rd number : "))
d = int(input("Enter the 4th number : "))

if(a > b and a > c and a >d):
    print("1st number is greatest number")
    
elif(b>a and b>c and b>d):
    print("2nd number is the gretatest number")
    
elif(c>a and c>b and c>d):
    print("3rd number is the greatest number.")
    
else:
    print("4th number is the greatest number.")
    
    
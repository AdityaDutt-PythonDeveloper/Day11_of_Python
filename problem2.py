# weather a student is passed or not in exam a student requires total 40% and atleast 33% in exam 

m1 = int(input("Enter the 1st subject marks : "))
m2 = int(input("Enter the 2nd subject marks: "))
m3 = int(input("Enter the 3rd subject marks : "))

avg = (m1 + m2 + m3)/3

if((m1>33) and (m2>33) and (m3>33) and (avg>40)):
    print("Student is passed!")
else:
    print("Student is failed...")
    
    
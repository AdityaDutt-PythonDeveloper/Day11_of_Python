# weather a string contains less than 10 characters or not/
name = input("Enter the username : ")

length = len(name)
# print(length)
if(length<10):
    print("A valid username.")
else:
    print("Username is not valid!")    

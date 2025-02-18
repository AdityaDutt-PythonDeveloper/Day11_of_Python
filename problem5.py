# wap to check weather a name is present in list or not?
name = input("Enter the username : ")
List = ['Aditya', "sood", "chawla", 'bansal']

if(name in List):
    print("Username exists in Database!")
else:
    print("name do not exists!")
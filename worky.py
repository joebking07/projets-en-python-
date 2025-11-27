
name = input("enter your name here: ")
print('hello', name)
age=input("enter your age: ")
age=int(age)
if age>18 :
    print('you are adult') 
else:
    if age==18:
        print('you are just major ')
    else:
        print("you're a minor")
        print("you will be adult in ",18-age,"year")
        print('thank you')
        
        
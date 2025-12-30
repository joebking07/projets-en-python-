
def security():
    



    while True:
       # header of code
      name = input('enter your name:')
      print('hello',name) 


      password=int(input("enter your password: "))

      if password:
          
       print("votre code peut etre valider")

        
   
      else: 
        
        return password
      
      print("error: retry to login")


      required_for_login=input("enter your information name_contact_occupation_residence").split("_")

      print('your name is:{}')


if __name__=="__main__":
  security()


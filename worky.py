
def verification ():
    
   
   
   while True:
      
      
      
      try:
         name= str(input("enter your name here: "))
         
         age=int(input("enter your age: "))
         
      except ValueError:
         print('your name or age is invalid\n now retry')
         continue

      if name:

         print('hello',name)   
      if age>18 :
         print('you are adult') 
      elif age==18:

         print('you are just major ')
      else:
         print("you're a minor")
         print(f"you will be adult in {18-age} year")
         print('thank you') 

   print('bye & thanks for your service')   
   
   
   

if __name__=='__main__':
  verification()

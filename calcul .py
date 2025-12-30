
def operations ():
    while True:
        print("bienvenue dans le menu des operations")
        print("1 -addition ")
        print("2-soustraction")
        print("3 - multiplication")
        print("4 - division")

        choix= int(input('faites votre choix ici'))

        if choix in [1,2,3,4]:
           nombre1=float(input('enter your firts number:'))
           nombre2=float(input(' enter your second number:'))
          
           if choix==1 :
            
            result=nombre1+nombre2
        
        
           elif choix==2:
            
               result=nombre1-nombre2 
         
         

           if choix==3:
            
              result=nombre1*nombre2
         
              print('the result is ',result)


           if choix==4:
              
              result=nombre1/nombre2

              
        else:

            print(" s'il vous plait refaite votre choix ")

            continue

if __name__=="__main__":
    operations()


            
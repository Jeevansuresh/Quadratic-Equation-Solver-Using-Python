import math
import time 
def hello():
    
 a = int(input("Enter a = "))
 b = int(input("Enter b = "))
 c = int(input("Enter c = "))
 e = -b +((((b**2)-(4*a*c))**0.5))
 f = -b -((((b**2)-(4*a*c))**0.5))
 d = (2*a)
 x = e/d
 y = f/d
 print("The First Value Is",x)
 print()
 print("The Second Value Is",y)
 print()
 time.sleep(2)
hello()
while 1:
 query = input("Do You Want To Try Once Again y/n ?")
 query = query.lower()
 if (query =='y'):
    hello()
 elif (query =='n'):
   print("Ok Thanks,Can You Provide Ratings On My Accuracy On A Scale Of 1 to 5")
   def start():
     r = int(input("Enter Ratings"))
     if (r==1):
        print("Oops Thanks For The Suggestion")
     elif (r==2):
        print("Well,I Will Try To Improve Myself")
     elif (r==3):
        print("Thank You For Your Ratings")
     elif (r==4):
        print("Thank You")
     elif (r==5):
        print("Thank You :)")
     else :
        print("Invalid Option")
        time.sleep(1)
        print()
        print("Try again")
        time.sleep(1)
        print()
        start()
   start()
   exit()

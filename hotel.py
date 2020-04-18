# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 18:58:15 2020

@author: swetha
"""

class Hotelmgmt:
    global at
    global amt1
    global amt2
    global a
    global amt
    global name
    global date
    n=1
    at=0
    amt1=0
    amt2=0
    amt=0
    
    def details(self):
        global date
        global name
        name=input("Enter your name : ")
        addr=input("Enter your address:  ")
        no=int(input("No. of members:   "))
        date=input("Check in date:  ")
        time=input("Time :   ")
        
    def types(self):
        global a
        a=0
        t=1
        while(t==1):
            print("What type of room do you prefer? ")
            print(" 1.Standard single")
            print(" 2.Deluxe double")
            print(" 3.Economy triple")
            print(" 4.Royal suite")
            
            
            try:
                ch=int(input("Enter your choice : "))
                if(ch==1):
                    print("\nYou have successfully booked STANDARD SINGLE which cost Rs.500 per day")
                    a=a+500
                elif(ch==2):
                    print("\nYou have successfully booked DELUXE DOUBLE which cost Rs.1000 per day")
                    a=a+1000
                elif(ch==3):
                    print("\nYou have successfully booked ECONOMY TRIPLE which cost Rs.1500 per day")
                    a=a+1500
                elif(ch==4):
                    print("\nYou have successfully booked ROYAL SUITE which cost Rs.2500 per day")
                    a=a+2500
                else:
                    print("Enter valid input")
                    ch=int(input("Enter your choice : "))
                    if(ch==1):
                        print("\nYou have successfully booked STANDARD SINGLE which cost Rs.500 per day")
                        a=a+500
                    elif(ch==2):
                        print("\nYou have successfully booked DELUXE DOUBLE which cost Rs.1000 per day")
                        a=a+1000
                    elif(ch==3):
                        print("\nYou have successfully booked ECONOMY TRIPLE which cost Rs.1500 per day")
                        a=a+1500
                    elif(ch==4):
                        print("\nYou have successfully booked ROYAL SUITE which cost Rs.2500 per day")
                        a=a+2500
            except ValueError:
                 print("Please enter input as suggested.")
            ch1=input("Do you want wifi connection in your room? (yes or no) (extra charges applied)")   
            if(ch1=="yes"):
                a=a+100
            t=int(input("\nIf you want to book any other rooms? If yes,press 1 "))
                
               
            
          
    def food(self):
        global amt
        amt=0
        r=1
        while (r==1):
            print ("What would you like to have?")
            print ("enter 1 for breakfast","enter 2 for lunch","enter 3 for dinner","enter 4 for beverages",sep='\n')
            c=int(input("enter your choice:"))
            if (c==1):
                print("code","items    ","price",sep='\t')
                print("1","idli       ","Rs.20",sep='\t')
                print("2","dosa       ","Rs.50",sep='\t')
                print("3","pongal     ","Rs.35",sep='\t')
                print("4","poori      ","Rs.35",sep='\t')
                print("5","chapathi   ","Rs.22",sep='\t')
                print("6","bread omlet","Rs.25",sep='\t')
                print("7","vadai      ","Rs.12",sep='\t')
                item=int(input("enter the code of the item you want"))
                q=int(input("enter the quantity of the selected item"))
                if (item==1):
                    amt=amt+(q*20)
                if (item==2):
                    amt=amt+(q*50)
                if (item==3 or item==4):
                    amt=amt+(q*35)
                if (item==5):
                    amt=amt+(q*22)
                if (item==6):
                    amt=amt+(q*25)
                if (item==7):
                    amt=amt+(q*12)
                
            elif(c==2):
                print("code","items            ","price",sep='\t')
                print("1","meals              ","Rs.90",sep='\t')
                print("2","sambar rice        ","Rs.50",sep='\t')
                print("3","curd rice          ","Rs.40",sep='\t')
                print("4","biriyani(veg)      ","Rs.100",sep='\t')
                print("5","chicken biriyani   ","Rs.150",sep='\t')
                print("6","fried rice(veg)    ","Rs.110",sep='\t')
                print("7","fried rice(chicken)","Rs.160",sep='\t')
                item=int(input("enter the code of the item you want"))
                q=int(input("enter the quantity of the selected item"))
                if (item==1):
                    amt=amt+(q*90)
                if (item==2):
                    amt=amt+(q*50)
                if (item==3):
                    amt=amt+(q*40)
                if (item==4):
                    amt=amt+(q*100)
                if (item==5):
                    amt=amt+(q*150)
                if (item==6):
                    amt=amt+(q*110)
                if (item==7):
                    amt=amt+(q*160)
                
                
            elif(c==3):
                print("code","items            ","price",sep='\t')
                print("1","idli               ","Rs.20",sep='\t')
                print("2","dosa               ","Rs.50",sep='\t')
                print("3","chapathi           ","Rs.22",sep='\t')
                print("4","parotta            ","Rs.30",sep='\t')
                print("5","fried rice(veg)    ","Rs.110",sep='\t')
                print("6","fried rice(chicken)","Rs.160",sep='\t')
                print("7","noodles(veg)       ","Rs.135",sep='\t')
                item=int(input("enter the code of the item you want"))
                q=int(input("enter the quantity of the selected item"))
                if (item==1):
                    amt=amt+(q*20)
                if (item==2):
                    amt=amt+(q*50)
                if (item==3):
                    amt=amt+(q*22)
                if (item==4):
                    amt=amt+(q*30)
                if (item==5):
                    amt=amt+(q*110)
                if (item==6):
                    amt=amt+(q*160)
                if (item==7):
                    amt=amt+(q*135)
                
            else:
                print("code","items                      ","price",sep='\t')
                print("1","milk                         ","Rs.20",sep='\t')
                print("2","tea                          ","Rs.18",sep='\t')
                print("3","coffee                       ","Rs.22",sep='\t')
                print("4","vegetable soup               ","Rs.40",sep='\t')
                print("5","juice(apple/mango/lemon)     ","Rs.60",sep='\t')
                print("6","juice(pomegranate/watermelon)","Rs.90",sep='\t')
                item=int(input("enter the code of the item you want"))
                q=int(input("enter the quantity of the selected item"))
                if (item==1):
                    amt=amt+(q*20)
                if (item==2):
                    amt=amt+(q*18)
                if (item==3):
                    amt=amt+(q*22)
                if (item==4):
                    amt=amt+(q*40)
                if (item==5):
                    amt=amt+(q*60)
                if (item==6):
                    amt=amt+(q*90)
            r=int(input("do you want to order ant other items?if yes press 1:" ))
            print("food bill",amt)
            
    def laundry(self):
        global amt1
        amt1=0
        t=1;
        while(t==1):
            print("Choose '1' for Normal wash")
            print("Choose '2' for Dry wash")
            print("Choose '3' for Baby care wash")
            choice=int(input("Enter your choice:"))
            if (choice==1):
                print("Amount= Rs.25 per kg")
                t1=int(input("Enter the weight in kgs"))
                a1=25*t1;
                amt1=amt1+a1;
                print("The total amount for normal wash is Rs.",a1)
            if (choice==2):
                print("Amount= Rs.50 per kg")
                t2=int(input("Enter the weight in kgs"))
                a2=50*t2;
                amt1=amt1+a2;
                print("The total amount for dry wash is Rs.",a2)
            if (choice==3):
                print("Amount= Rs.75 per kg")
                t3=int(input("Enter the weight in kgs"))
                a3=75*t3;
                amt1=amt1+a3;
                print("The total amount for baby care wash is Rs.",a3)
             
            print("Do you want any other washing?")
            t=int(input("If yes enter 1 (Else enter 0)"));
        print("The total amount for laundry is Rs.",amt1)
        
    def maintenance(self):
        print("Do you need any other service?")
        print("If yes enter 1 (Else enter 0)")
        x=int(input("Enter your choice:"))
        if (x==1):
            print("Your service is on the way!")
        else:
            print("We are ready to serve you any time.")
        
        print("Do you have any complaints?")
        print("If yes enter 1 (Else enter 0)")
        y=int(input("Enter your choice:"))
        if (y==1):
            print("Sorry for the inconvenience.We will rectify our mistakes.This will not be repeated again.")
        else:
            print("Thank you.")
            
        print("Would you like to give feedback?")
        print("If yes enter 1 (Else enter 0)")
        z=int(input("Enter your choice:"))
        if(z==1):
            s=input("Feedback please")
            print("Thank you for your feedback!")


    def checkout(self):
        global amt2
        global a
        amt2=0        
        n=int(input("Enter the number of days of your stay"))      
        amt2=a*n
        print("\nThe bill for your stay",amt2)
        
    def display(self):
        global at
        global name
        at=0
        tax=15;
        at=amt1+amt2+amt+tax;
        print("\n\n")
        print("*******************************************************")
        
        print("\nBill details\n")
        print("S.No\tService    \tAmount")
        print("1.  \tRoom rent  \t",amt2)
        print("2.  \tFood bill  \t",amt)
        print("3.  \tLaundry    \t",amt1)
        print("4.  \tTax        \t",tax)
        print("\n TOTAL",at)
        print("Thank you.Visit again,Pleasure to serve you ",name)
        
        
        
        
        
        
def main():
    print("  ***********************************************   ")
    print("             WELCOME TO THE PARADISE                ")
    print("  ***********************************************   ")
    print("\n \n")
    x=Hotelmgmt();
    print("\nPlease enter the details\n")
    x.details();
    print("\nPlease specify the booking details\n")
    x.types();
    t=1;
    while(t==1):
        print("1.FOOD\n2.LAUNDRY SERVICES\n3.MAINTENANCE\n4.CHECKOUT\n")
        
        ch=int(input("Enter your choice"))
        if(ch==1):
            x.food();
        if(ch==2):
            x.laundry();
        if(ch==3):
            x.maintenance();
        if(ch==4):
            x.checkout();
            break
           
        t=int(input("\nIf you want our services or checkout  press 1 (or 0 if not)"))
    x.display();  
if __name__=="__main__":
        main()        
        
    
            
        
    
            
            


       
    
    
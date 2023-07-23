# importing external module to get acesss in this module
import Return
import CostumeList
import DateTime
import Rent

#function name Store is created to use in other module
def Store():
    while(True):
        print(''' xxxxxxxxxxxxxxxxxxxxxxxxx Welcome to Costume Rental System.xxxxxxxxxxxxxxxxxxxxxxxxx
- Press 1: To Display the Costumes available.
- Press 2: To Renting Process.
- Press 3: To Return Costumes you rented.
- Press 4: To Exit from the System.''')

        #try,except block for exception handeling
        try:
            n = int(input("Enter your choice: "))
            print()
            # conditional statements for making desicion inside the program
            if(n==1):
                CostumeList.list()
                print("The available Costumes are : \n")
                print(f"Number {' '*5} Costume-Name {' '*15} Costume-Brand {' '*15} Quantity {' '*17} Price \n")
                file=open("Costume.txt","r")
                for i in range(3):
                    id = CostumeList.ID[i]
                    name =  CostumeList.CostumeName[i]
                    quantity = CostumeList.Quantity[i]
                    brand = CostumeList.Brand[i]                    
                    price = CostumeList.Price[i]
                    print(str(id)+" "*(14-len(id))+ name+" "*(29-len(name))+ brand+" "*(29-len(brand))+quantity+" "*(29-len(quantity))+"$"+price+"\n")
                print()
                file.close()
                
            elif(n==2):
                CostumeList.list()
                Rent.RentCostume()
                
            elif(n==3):
                CostumeList.list()
                Return.ReturnCostume()
                
            elif(n==4):
                print("Thank you for using our Costume Retnal system")
                break
            
            else:
                print("Please enter a number of your choice from1-4")
        except ValueError:
            print("\nPlease input the valid number.")
#closing the function
Store()


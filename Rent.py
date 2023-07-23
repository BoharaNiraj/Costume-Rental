from tkinter.tix import CheckList
import DateTime
import CostumeList

def RentCostume():
    Rented=False
    while(True):
        firstname=input("Input the first name of the Renter: ")
        if firstname.isalpha():
            break
        print("Please input alphabet only")
    while(True):
        lastname=input("Input the last name of the Renter: ")
        if lastname.isalpha():
            break
        print("Please input alphabet only")
            
    Rent="Rented by-"+firstname+".txt"
    file=open(Rent,"w+")
    file.write("\t\t\t Costume Management System. \n")
    file.write("\n*****************************************************************************")
    file.write("\n\t\t Details of the Renter and Costume Rented\n")
    file.write("\t\t Rented By: "+ firstname+" "+lastname+"\n")
    file.write("\t\t Date and Time: " + DateTime.getDateTime()+"\n\n")
    file.write(f"S.N. {' '*20} Costume Name {' '*20} Brand {' '*20} Quantity {' '*20} Price\n" )
    file.close()

    total=0.0
    while Rented==False:
        print("\nPlease select a option below:\n")
        for i in range(3):
            print("Input",i, "to Rent Costume", CostumeList.CostumeName[i])        
        try:   
            a=int(input())
            if a<0:
                print("Invalid input!!!")
            try:
                if(int(CostumeList.Quantity[a])>0):
                    print("\nThe Costume you've selected is in stock.\n")
                    file=open(Rent,"a")
                    id = CostumeList.ID[a]
                    name =  CostumeList.CostumeName[a]
                    brand = CostumeList.Brand[a]
                    quantity = CostumeList.Quantity[a]
                    price = CostumeList.Price[a]
                    file.write(str(id)+" "*(29-len(id))+ name+" "*(29-len(name))+ brand+" "*(29-len(brand))+str(quantity)+" "*(29-len(quantity))+"$"+str(price)+"\n")
                    file.close()    
                    amount=int(input("select the amount you want to rent: "))
                    CostumeList.Quantity[a]=int(CostumeList.Quantity[a])-amount
                    total=total+(int(CostumeList.Price[a]))*amount                
                    file=open("Costume.txt","w+")
                    for i in range(3):
                        file.write(str(CostumeList.ID[i])+","+CostumeList.CostumeName[i]+","+str(CostumeList.Quantity[i])+","+CostumeList.Brand[i]+","+"$"+str(CostumeList.Price[i])+"\n")
                    file.close()
                    #multiple Costume Renting code
                    Rented2=True
                    count=1
                    while Rented2==True:
                        choice=str(input("If you want to Rent another Costume then press Y for Yes if not then press N for No: \n").upper())
                        if(choice=="Y"):
                            count+=1            
                            print("\nPlease select an option below:\n")
                            for i in range(len(CostumeList.CostumeName)):
                                print("Input", i, "to Rent Costume", CostumeList.CostumeName[i])
                            try:
                                b=int(input())
                                if b==a:
                                    print("I am sorry. You can't Rent the same Costume twice.")
                                    count=count-1
                                else:
                                    try:
                                        if(int(CostumeList.Quantity[b])>0):
                                            print("\nThe Costume you've selected is in stock.\n")
                                            file=open(Rent,"a")
                                            file.write(str(CostumeList.ID[b])+". \t\t"+ CostumeList.CostumeName[b]+"\t\t\t  "+CostumeList.Brand[b]+" \t\t  "+"$"+CostumeList.Price[b]+"\n")
                                            file.close()
                                            amount=int(input("select the amount you want to rent: "))
                                            CostumeList.Quantity[a]=int(CostumeList.Quantity[b])-amount
                                            total+=(int(CostumeList.Price[b]))*amount
                                            file=open("Costume.txt","w+")
                                            for i in range(3):
                                                file.write(str(CostumeList.ID[i])+","+CostumeList.CostumeName[i]+","+str(CostumeList.Quantity[i])+","+CostumeList.Brand[i]+","+"$"+str(CostumeList.Price[i])+"\n")
                                            file.close()
                                            Rented=False
                                        else:
                                            print("Costume is not available right now. Please visit us after some time.")
                                            Rented2=False
                                            break
                                    except IndexError:
                                        print("\nPlease choose Costume acording to their number.")
                            except ValueError:
                                print("\nPlease input as suggested.")
                        elif(choice=="N"):
                            print("\nThank you for using our service to Rent Costume from us. ")
                            print("")
                            Rented2=False
                            Rented=True
                        else:
                            print("Please input as suggested")         
                else:
                    print("Costume is not available right now. Please visit us after some time.")
                    Rented=False
                    
                file=open(Rent,"a")
                file.write("\n\t\t\t\t\t\t\t\t\tTotal: $"+ str(total))
                file.write("\n*************************************************************************************************************************")
                file.write("\nTHANK YOU FOR YOUR TIME HERE.\nWE HOPE TO SEE YOU AGAIN")
                file.write("\n*************************************************************************************************************************")
                file.close()
            except IndexError:
                print("\nPlease choose Costume acording to their number.")
        except ValueError:
            print(f"\nPlease input as suggested.")

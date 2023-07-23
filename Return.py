import CostumeList
import DateTime
def ReturnCostume():
    name=input("Enter name of borrower: ")
    a="Rented by-"+name+".txt"
    try:
        file=open(a,"r")
        lines=file.readlines()
        lines=[a.strip("$") for a in lines]
        file.close()
    
        file=open(a,"r")
        data=file.read()
        print(data)
    except:
        print("The borrower name is incorrect or not registered.")
        ReturnCostume()

    Return="Returned by-"+name+".txt"
    file=open(Return,"w+")
    file.write("\t\t\tCostume Management System\n")
    file.write("\n********************************************************************")
    file.write("\n\t\t Details of the returner and Costume returned\n")
    file.write("\t\t\t Returned By: "+ name+"\n")
    file.write("\t\t\t Date and Time: " + DateTime.getDateTime()+"\n\n")
    file.write("S.N. \t\t Costume Name \t\t Price\n")
    file.close()
    count=0
    total=0.0
    for i in range(3):
        if CostumeList.CostumeName[i] in data:
            count=count+1
            file=open(Return,"a")
            file.write(str(count)+" \t\t "+CostumeList.CostumeName[i]+" \t\t"+" $"+CostumeList.Price[i]+"\n")
            file.close()
            CostumeList.Quantity[i]=int(CostumeList.Quantity[i])+1
            total+=int(CostumeList.Price[i])
            
    print("The Costume return date expires in 5 days. Has the Costume return date already expired?")
    print("Press Y for Yes and N for No")
    choice=input().upper
    if(choice()=="Y"):
        print("By how many days was the Costume returned late?")
        day=int(input())
        fine=3*day
        file=open(Return,"a")
        file.write("\n\t\t\t\t\tfileine: $"+ str(fine)+"\n")
        file.close()
        total=total+fine

    print("Total: "+ "$"+str(total))
    file=open(Return,"a")
    file.write("\t\t\t\t\ Total: $"+ str(total))
    file.write("\n*************************************************************************************************************************")
    file.write("\nTHANK YOU fOR YOUR TIME HERE.\nWE HOPE TO SEE YOU AGAIN")
    file.write("\n*************************************************************************************************************************")
    file.close()
    
        
    file=open("Costume.txt","w+")
    for i in range(3):
        file.write(CostumeList.ID[i]+","+CostumeList.CostumeName[i]+","+str(CostumeList.Quantity[i])+","+CostumeList.Brand[i]+","+"$"+CostumeList.Price[i]+"\n")
    file.close()

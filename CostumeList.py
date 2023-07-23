ID = []
CostumeName=[]
Quantity=[]
Brand=[]
Price=[]

def list():
    file=open("Costume.txt","r")
    lines=file.readlines()
    lines=[a.strip('\n') for a in lines]
    for i in range(len(lines)):
        x=0
        for j in lines[i].split(','):
            if(x==0):
                ID.append(j)
            elif(x==1):
                CostumeName.append(j)
            elif x==2:
                Quantity.append(j)
            elif(x==3):
                 Brand.append(j)                
            elif(x==4):
                Price.append(j.strip("$"))
            x+=1

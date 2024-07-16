import os.path
class Person():
    __member_id=0
    __id_member=0
    def __init__(self,email_address,name,password,address,phonenum):
        Person.__member_id+=1
        self.__id_member=Person.__member_id
        self.email_address=email_address
        self.name=name
        self.password=password
        self.address=address
        self.phonenum=phonenum
    def show(self):
        print(self.__id_member)
        print(self.email_address)
        print(self.name)
        print(self.password)
        print(self.address)
        print(self.phonenum)
    def getter():
        print(Person.__member_id)
class Buyer(Person):
    def __init__(self, email_address, name, password, address, phonenum,shipping_address):
        super().__init__(email_address, name, password, address, phonenum)
        self.shipping_address=shipping_address
    def show(self):
        super().show()
        print(self.shipping_address)

class Seller(Person):
    def __init__(self, email_address, name, password, address, phonenum,bankaccnum,routnum):
        super().__init__(email_address, name, password, address, phonenum)
        self.bankaccnum=bankaccnum
        self.routnum=routnum
    def show(self):
        super().show()
        print(self.bankaccnum)
        print(self.routnum)


seller=Seller("Email","Name","Password","Address","Phonenum","BankAccnum","Routnum")
seller2=Seller("Email","Name","Password","Address","Phonenum","BankAccnum","Routnum")
buyer=Buyer("Email","Name","Password","Address","Phonenum","Shipping Address")

   
def putinfile(info_array):
 #Pass an array to this 
 #Check if file exist otherwise it will create a new file
 if os.path.isfile("demofile2.txt"):
    f=open("demofile2.txt","a")
    for person in range(len(info_array)):
        g=info_array[person].get()
        if info_array[person].member=="Buyer":
            print("This is Append Buy")
            f.write("Buyer")
            f.write(str(g))
            f.write("\n")
        
        else:
            print("This is Append Sell")
            f.write("Seller")
            f.write(str(g))
            f.write("\n")
        
 
    f.close()
 else:
    f=open("demofile2.txt","w")
    for person in range(len(info_array)):
        g=info_array[person].get()
        if info_array[person].member=="Buyer":
            print("This is Write Buy")
            f.write("Buyer")
            f.write(str(g))
            f.write("\n")
        
        else:
            print("This is Write Sell")
            f.write("Seller")
            f.write(str(g))
            f.write("\n")
        
 
    f.close()

def get_info():
#Assign this to an array
#Check if the file exist and read the content otherwise it return nothing
   if os.path.isfile("demofile2.txt"):
    info_array=[]
    with open("demofile2.txt","r") as f:
        while True:
            line = f.readline()
            if not line:
                break
            else:
             info_array.append(eval(line))
    return info_array


#removables
info_array=get_info()
if not info_array:
    print("Empty Set")
else: 
    for info in info_array:
        info.show()


    

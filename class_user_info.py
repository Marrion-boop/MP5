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

    

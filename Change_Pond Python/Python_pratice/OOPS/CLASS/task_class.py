def task_1(values):
    class Prodect:
        _product_id = 0
        
        def  add_function(self,pname,pprice,pdesc):
            self.pname = pname
            self.pprice = pprice
            self.pdesc = pdesc
            Prodect._product_id += 1 
            self.__id = self._product_id
            print("Prodect add sucessfully")
        def get_product_names(self):
            print(f"product name: {self.pname}")
            print(f"product price: {self.pprice}")
            print(f"product description: {self.pdesc}")
            print(f"product id: {self.__id}")
    
    
    for trash in range(1,values+1):
        
    product_1 = Prodect()
    product_1.add_function(pname=input("Enter the product name: "),
                           pprice=int(input("Enter the product price: ")),
                           pdesc=input("Enter the product description: "))
    product_1.get_product_names()
    product_2 = Prodect()
    product_2.add_function(pname=input("Enter the product name: "),
                           pprice=int(input("Enter the product price: ")),
                           pdesc=input("Enter the product description: "))
    product_2.get_product_names()
    product_3 = Prodect()
    product_3.add_function(pname=input("Enter the product name: "),
                           pprice=int(input("Enter the product price: ")),
                           pdesc=input("Enter the product description: "))
    product_3.get_product_names()
    product_4 = Prodect()
    product_4.add_function(pname=input("Enter the product name: "),
                           pprice=int(input("Enter the product price: ")),
                           pdesc=input("Enter the product description: "))
    product_4.get_product_names()

def main():
    task_1(int(input("How many Product you like to add: ")))

if __name__ == "__main__":
    main()
class Product:
    def __init__(self, product) -> None:
        self.product = product
    
    def add_product(self, product):
        self.product.append(product) 
        
    def get_product(self):
        print(self.product)

class Shop(Product):
    def __init__(self, name, product) -> None:
        self.name = name
        super().__init__(product)

    def buy_product(self, p_name):
        if p_name not in self.product:
            print('No product available')
        else: print('congrats!')

dokan = Shop('dokan', [])
dokan.add_product('boi')
dokan.add_product('khata')
dokan.add_product('kolom')
# dokan.get_product()
dokan.buy_product('kuta')
dokan.buy_product('boi')
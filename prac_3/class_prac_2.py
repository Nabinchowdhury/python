class Product:
    def __init__(self, product) -> None:
        self.product = product
    
    def get_products(self):
        return self.product

class Shop:
    def __init__(self, name) -> None:
        self.name = name
        self.prod = []
    def add_product(self, product):
        self.prod.append(Product(product).get_products())
        
    def buy_product(self, p_name):
        if p_name not in self.prod:
           print('not available')
        else: print('paichi mama')
dokan = Shop('batighor')
dokan.add_product('onek gulo boi')
dokan.add_product('boi')
dokan.add_product('moi')
dokan.add_product('doi')
dokan.add_product('khoi')
dokan.buy_product('boiboi')
# notun_dokan = Shop('lightghor')
# notun_dokan.add_product('prochur boi')

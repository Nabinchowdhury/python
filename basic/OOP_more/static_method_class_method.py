class Shopping:
    def __init__(self, name = 'unknown') -> None:
        self.name = name

    @classmethod
    def purchase(self, item):
        print(f'purchasing : {item} from ')

    # def multiply(self, a, b):
    #     print(f'result is {a*b}')

    @staticmethod
    def multiply(a, b):
        print(f'result is {a*b}')
#class attribute / static attribute ====================
# basu = Shopping('Basundhara')
# basu.purchase('mobile')      
#===================================

#class method (@classmethod) ====================
# Shopping.purchase('basu', 'comp')   #if @classmethod is not declare
Shopping.purchase('laptop') #if @classmethod is not declare
#============================================

#static method(@staticmethod) ===============
# Shopping.multiply('add', 4,5 ) #if @staticmethod is not declare
Shopping.multiply(4,6) #if @staticmethod is not declare
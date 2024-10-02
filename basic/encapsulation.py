#encapsulation
class Bank:
    def __init__(self, holder_name, initial_deposit) -> None:
        self.holder_name = holder_name
        self.__balance = initial_deposit  #immutable __balance/ private
    def getBalance(self):
        return self.__balance
name = Bank('nabin', 10000)  
print(name.getBalance())
# print(name.__balance) #not accessible
print(dir(name))
print(name._Bank__balance) #accesible

# (__) => two underscore = private e.g. self.__balance = initial_deposit [immutable __balance from outside]
# (_) => one underscore = protected e.g. self.holder_name = holder_name
# () => no underscore = public e.g. self._branch = branch
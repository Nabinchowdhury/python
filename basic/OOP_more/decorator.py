import math

def timer(func):
    def inner(*args, **kwargs):
        print('inside inner start')
        func(*args, **kwargs)
        print('inside inner end')
    
    return inner

# def get_factorial():
#     print('factorial started')
# timer(get_factorial)()  
# or

@timer
def get_factorial(n = 120):
    print('factorial started')
    res = math.factorial(n)
    print(res)

get_factorial(5)
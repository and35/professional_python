"""lets create a decorator which indicates the time excecution of an especific function"""
import time 

def decorator_execution_time(func):
    def wrapper(*args,**kwargs): # wrapper = envoltura
        start_time = time.time()
        func(*args,**kwargs)
        final_time = time.time()
        time_elapsed = final_time - start_time
        print("code takes: {}s  \n{}".format(time_elapsed, "_"*50))
    return wrapper


# 1 lets see how much takes pass a million range
@decorator_execution_time
def random_funct(): 
    for _ in range(1000000):     
        pass
    print("using for in a  million range ")
random_funct()  

"""2 lets see how much takes a sum function
we must add sum paramaters in wrapper func but if we add we will use in random:funct also 
 so to solve it, we put the parameters as something variable 
 *args: no importa los argumentos posicionales, la funcion los resivira
 **kwargs: no importa los argumentos nombrados, la funcion los resivira"""
@decorator_execution_time 
def sum(a : int, b: int) -> int: 
    print(a + b)
sum(5,5)

""" 3 lets see how much take a hello function """
@decorator_execution_time 
def hello(name="andres"): # in this case is where **kwargs works 
    print("hello {} ".format(name))
hello()




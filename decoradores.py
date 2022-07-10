
"""tenemos una funcion que crea un saludo y creamos un 
decorador que le agrega la fecha a la funcion del saludo"""
import time
def decorador(saludo):
    def envoltura(nombre): # el parametro que se pasara a saludo se esccifica aqui  
        print(time.strftime("%d/%m/%y")) # pieza de codigo  que se añade al codigo original  
        saludo(nombre)
    return envoltura

@decorador
def saludo(nombre):
    print("hola {}".format(nombre))
    
saludo(input("dime tu nombre: "))


 

"""tenemos una funcion que crea un saludo y creamos un 
decorador que le agrega la fecha a la funcion del saludo"""
import time
def decorador(saludo):
    def envoltura(nombre): # se le llama envoltura a la funcion que envolvera a saludo 
        print(time.strftime("%d/%m/%y")) # pieza de codigo  que se añade al codigo original  
        saludo(nombre)
    return envoltura

@decorador
def saludo(a):
    print("hola {}".format(a))
    
saludo(input("dime tu nombre: "))


 
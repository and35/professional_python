# inputs a provar 
hi = "hola"
p = "anita lava la tina"
num = 1000

# version basica 
def is_palindrome(word):
    word = word.replace(" ", "").lower() # limpiamos el input quitando espacios y estandarizando a minusculas
    return word[::-1] == word
#print(is_palindrome(num))

# version pro 
def is_palindrome_2(word: str) -> bool:# definimos el tipo de dato del input y return de la funcion 
    word = word.replace(" ", "").lower() 
    return word[::-1] == word
print(is_palindrome_2(num))

# creamos una funcion que repirira n veces el string dado
def multStrings(n):
    def nestedStr(s):
        assert type(s) == str, "solo puedes usar cadenas" # condicion de error 
        return s * n
    return nestedStr

times3 = multStrings(3)
times10 = multStrings(10)
print(times10("ja"))

"""" ejercicio 2 hacer un divisor"""
def make_division_by(n):
    def divisor(d):
        return d/n
    return divisor

division_by_3 = make_division_by(3)
print(division_by_3(12))


def make_division(d,n):
    return d/n
print(make_division(15,3))

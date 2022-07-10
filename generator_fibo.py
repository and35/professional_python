# 1 lets do the phibo iterators using generators:
def fibo_gen(n_max):
    n1=0
    n2=1
    counter=0
    while True:
        if n_max != counter:

            if counter == 0:
                counter+=1
                yield n1
            if counter == 1:
                counter+=1
                yield n2
            else:
                counter+=1
                aux = n1 + n2
                n1, n2 = n2, aux
                yield n2
        else:
            break 
phi = fibo_gen(10)

for a in phi:
    print(a)

# 2 ten en cuenta que se pudo comprimir aun mas a solo
def fibonacci_gen(max):
    a, b, c = 0, 1, 0
    while True:
        yield a
        a, b, c= b, a+b, c+1
        if c == max: break

phi2 = fibonacci_gen(10)

for a in phi2:
    print(a)

# 3 using  generator expresion 
print("-"*100)
import math
def fibo_gen_3(n_max):
    return (round(((1.618033988749895**x) - (1 - 1.618033988749895)**x )/(math.sqrt(5))) for x in range(n_max))
for a in fibo_gen_3(10): print(a)

"""print("-"*100)
phi_num = (1+math.sqrt(5))/2#1.618033988749895
print(phi_num)
pi = lambda x: round(((phi_num**x) - (1 - phi_num)**x )/(math.sqrt(5)))
for i in range(150):
    print(pi(i))"""
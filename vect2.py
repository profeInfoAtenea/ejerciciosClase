import random
'''Crea un script llamado vect2.py con funciones
para rellenar un vector de 15 enteros:'''

'''
a) Con valores aleatorios entre 1 y 10,
y a continuación diga cuantos pares e impares hay.
'''
# Creamos una lista de 15 elementos cada uno de ellos 1 a 10.
def jose_lista_aleatoria():
    lista = [0] * 15
    contador = 0
    for i in range(0,15):
        lista[i] = random.randint(1,10)
    return lista


def david_lsita_aleatoria():
    lista_alpha = []
    i = 1
    while( i <= 15):
        x = random.randint(1,10)
        lista_alpha.append(x)
        i+=1
    return lista_alpha

def alternativa():
    return [random.randint(1,10) for x in range(0,15)]

lst = alternativa()

def apartado_a(lista):
    print(lista)
    pares = 0
    impares = 0
    x = 0
    while(x < 15):
        if(lista[x] % 2 == 0):
            pares += 1
        else:
            impares+= 1
        x = x + 1
    print("Pares: ", pares)
    print("Impares: ", impares)
    return [pares, impares]

'''
b) Con valores aleatorios entre 1 y 10,
y a continuación sume los que estén en
posiciones que son múltiplos de 3.
'''
def apartado_b(lista):
    acumulador = 0
    for i in range(0,15):
        if(i % 3 ==0):
            acumulador = acumulador + lista[i]
    print(lista)
    print("acumulador: ", acumulador)

def apartado_c():
   n = 15
   f = [0,1]
   x = 0
   res = 0
   for i in f:
       res = res + i
       f.append(res)
       x = x + 1
       if(x == n):
           break
   f.pop(0)
   f.pop(0)
   return f

def apartado_c_2():
    '''inicializo las variables '''
    vector = []
    x = 0
    fi1 = 1
    fi2 = 0
    res = 0
    
    vector.append(0)
    vector.append(1)
    while(x < 13):
        res = fi1 + fi2
        fi2 = fi1
        fi1 = res
        vector.append(res)
        x += 1
    return vector

def fibonacci(n):
    if(n == 1):
        return 1
    if(n == 0):
        return 0
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def apartado_c_3():
    return [fibonacci(x) for x in range(0,15)]

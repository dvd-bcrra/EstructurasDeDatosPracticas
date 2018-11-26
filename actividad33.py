import random

def shell(ari):
    salto = len(ari)//2
    while salto != 0:
        cambios  =  True
        while cambios:
            cambios = False
            for i in range(salto,len(ari)):
                if ari[i - salto] > ari[i]:
                    ari[i], ari[i - salto] = ari[i - salto], ari[i]
                    cambios = True
        salto = salto//2

arreglo = []
for i in range(50):
    arreglo.append(random.randint(0,100))
shell(arreglo)
print(arreglo)

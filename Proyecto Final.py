import random
from datetime import datetime

#BUBBLESORT
bubble = 0
def bubbleSort(arreglo):
    for i in range(0,len(arreglo)):
        for j in range(0,len(arreglo)-1-1):

            #si el valor siguiente es menor que el actual...
            if arreglo[j] > arreglo[j+1]:

                #el mayor se almacena en la burbuja
                bubble = arreglo[j+1]

                #el mayor se iguala al actual
                arreglo[j+1] = arreglo[j]

                #el actual se iguala a la burbuja
                arreglo[j] = bubble
#ENDBUBBLE

#QUICKSORT
def quickSort(ari,first,last):
    if first<last:
        sp = splitpoint(ari,first,last)
        quickSort(ari,first,sp - 1)
        quickSort(ari,sp + 1,last)

def splitpoint(ari,first,last):
    pvt = ari[first]
    left = first + 1
    right = last

    detenerse = False
    while not detenerse:

        while left <= right and ari[left] <= pvt:
            left = left + 1

        while ari[right] >= pvt and right >= left:
            right = right -1

        if right < left:
            detenerse = True
        else:
            #EXCHANGE
            burbuja = ari[left]
            ari[left] = ari[right]
            ari[right] = burbuja
                       
    #EXCHANGE ENTRE PIVOTE Y SPLITPOINT
    burbuja = ari[first]
    ari[first] = ari[right]
    ari[right] = burbuja
    return right
#ENDQUICK

#SHELLSORT
def shellSort(ari):
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
#ENDSHELL

#MERGESORT
def mergeSort(ari):
    #SI LA LONGITUD DEL ARREGLO ES 1, SE DEVUELVE TAL CUAL
    if len(ari) == 1:
        return ari

    #SINO, SE PARTICIONA EL ARREGLO LLAMANDO ESTE MISMO METODO
    #RECURSIVAMENTE
    else:
        mid = len(ari)//2
        izq = ari[:mid]
        der = ari[mid:]
        izq = mergeSort(izq)
        der = mergeSort(der)

        #SE MANDA A LLAMAR EL METODO DE MEZCLA
        return merge(izq,der)

def merge(izq,der):
    mezc = []
    while(len(izq) > 0 and len(der) > 0):
        if(izq[0] > der[0]):
            mezc.append(der[0])
            der = der[1:]
        else:
            mezc.append(izq[0])
            izq = izq[1:]

    while len(izq) > 0:
        mezc.append(izq[0])
        izq = izq[1:]

    while len(der) > 0:
        mezc.append(der[0])
        der = der[1:]

    return mezc
#ENDMERGE

#################################################################################

def average(arreglo):
    long = len(arreglo)
    suma = 0
    for i in range(long):
        suma = suma + arreglo[i]
    return (suma/long)
    
bAverage = []
qAverage = []
sAverage = []
mAverage = []

print("Calculando...")

#30 VECES
for i in range(30):
    ari = []
    #ARREGLO DE 1000 VALORES ALEATORIOS ENTRE 0 Y 999
    for j in range(1000):
        ari.append(random.randint(0,1000))
    #TIEMPO INICIAL
    start = datetime.now()
    bubbleSort(ari)
    #TIEMPO FINAL
    end = datetime.now()
    #TIEMPO NETO (FINAL - INICIAL)
    time = (end - start).microseconds
    #LOS TIEMPOS SE ALMACENAN EN UN ARREGLO
    bAverage.append(time)

#SE EJECUTA LA MISMA OPERACION PARA CADA UNO DE LOS OTROS
#METODOS

for i in range(30):
    ari = []
    for j in range(1000):
        ari.append(random.randint(0,1000))
    start = datetime.now()
    quickSort(ari,0,len(ari)-1)
    end = datetime.now()
    time = (end - start).microseconds
    qAverage.append(time)

for i in range(30):
    ari = []
    for j in range(1000):
        ari.append(random.randint(0,1000))
    start = datetime.now()
    shellSort(ari)
    end = datetime.now()
    time = (end - start).microseconds
    sAverage.append(time)

for i in range(30):
    ari = []
    for j in range(1000):
        ari.append(random.randint(0,1000))
    start = datetime.now()
    mergeSort(ari)
    end = datetime.now()
    time = (end - start).microseconds
    mAverage.append(time)

#SE DESPLIEGAN LOS TIEMPOS DE CADA UNO DE LOS METODOS
print("BubbleSort\tQuickSort\tShellSort\tMergeSort")
for i in range(30):
    print(str(bAverage[i]) + "\t\t" +
          str(qAverage[i]) + "\t\t" +
          str(sAverage[i]) + "\t\t" +
          str(mAverage[i]))

print("Los metodos de ordenamiento fueron ejecutados 30 veces con 30 arreglos diferentes")
print("Cada arreglo con mil valores aleatorios")
print("Los datos corresponden al tiempo por cada uno en microsegundos (10^-6 seg)")

#SE IMPRIMEN LOS PROMEDIOS
print("-- Promedios --\n" +
      "Bubble sort: " + str(average(bAverage)) + "\n"
      "Quick sort: " + str(average(qAverage)) + "\n"
      "Shell sort: " + str(average(sAverage)) + "\n"
      "Merge sort: " + str(average(mAverage)))

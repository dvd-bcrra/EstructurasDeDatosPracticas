arreglo = [32,34,54,56,76,78,90,1,234]
bubble = 0

#ordenamiento
for i in range(0,len(arreglo)):
    for j in range(0,len(arreglo)-1):

        #si el valor siguiente es menor que el actual...
        if arreglo[j] > arreglo[j+1]:

            #el mayor se almacena en la burbuja
            bubble = arreglo[j+1]

            #el mayor se iguala al actual
            arreglo[j+1] = arreglo[j]

            #el actual se iguala a la burbuja
            arreglo[j] = bubble

#se imprimen
for i in range(0,len(arreglo)):
    print(arreglo[i])

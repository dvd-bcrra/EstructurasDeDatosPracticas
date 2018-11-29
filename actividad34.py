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

ari = [100,54,7,2,5,4,1]
print(mergeSort(ari))

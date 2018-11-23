import random

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

########################################################
ari = []
for i in range(50):
    ari.append(random.randint(0,100))
quickSort(ari,0,len(ari)-1)

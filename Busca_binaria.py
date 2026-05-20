#Busca Binária
def busca_binaria(item, lista):
    primeiro_elemento = 0
    ultimo_elemento = len(lista)-1
    meio = 0
    
    while primeiro_elemento <= ultimo_elemento:
        meio = (primeiro_elemento + ultimo_elemento) // 2
        if lista[meio] == item:
            return True
        elif lista[meio] < item:
            primeiro_elemento = meio + 1
           
        elif lista[meio] > item:
            ultimo_elemento = meio - 1
    return False
           
resultado = busca_binaria(item, [lista])

if resultado:
    print("O elemento está na lista")
else:
    print("O elemento NÃO está na lista")           

print(busca_binaria(item, [lista]))


        

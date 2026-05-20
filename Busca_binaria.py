#Busca Binária
def busca_binaria(item, lista):
    primeiro_elemento = 0
    ultimo_elemento = len(lista)-1
    meio = 0
    
    while primeiro_elemento <= ultimo_elemento:
        meio = (primeiro_elemento + ultimo_elemento) // 2
        print(primeiro_elemento, ultimo_elemento, meio) #Acompanhar estados das variáveis
        if lista[meio] == item:
            return True
        elif lista[meio] < item:
            primeiro_elemento = meio + 1
           
        elif lista[meio] > item:
            ultimo_elemento = meio - 1
            
           
print(busca_binaria(8, [1, 5, 8, 9, 19, 22, 28, 29]))

                   

            
        

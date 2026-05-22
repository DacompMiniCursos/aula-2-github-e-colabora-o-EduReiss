#Busca Binária
while True: #Laço de repetição para manter o código rodando enquanto o usuátio quiser consultar números na lista
    print("-" * 10) #Função para o usuário inputar o número e a lista que deseja buscar
    item = int(input("Digite o número que deseja buscar: "))
    print("-" * 10) 
    lista = list(map(int, input("Digite os números da lista em que você deseja buscar (separados por espaço): ").split()))
    lista.sort()
    
    def busca_binaria(item, lista): #função de busca binária
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
            
    resultado = busca_binaria(item, lista)

    if resultado:
        print("-" * 10) 
        print("O elemento está na lista")
        print("-" * 10) 
    else:
        print("-" * 10) 
        print("O elemento NÃO está na lista")   
        print("-" * 10) 

    continuar = input("Deseja buscar novamente? Digite (s/n): ") #Perguntar se o usuário deseja realizar outra busca ou encerrar o programa
    if continuar.lower() != "s":
        print("Obrigado por usar o programa!")
        break

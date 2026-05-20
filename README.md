#Como funciona uma busca binária

Para entender de forma prática, imagine que você está procurando a palavra "Programação" em um dicionário: 
Você abre o livro exatamente no meio e vê a letra "M". 
Compara: Como "P" vem depois de "M", você sabe que a palavra não está na primeira metade do dicionário.
Divide e repete: Você descarta a primeira metade e foca apenas na segunda metade. 
Você abre o meio dessa nova parte e repete o processo até encontrar a palavra exata.

# Por que usar a Busca Binária?
*Velocidade extrema:* Em vez de verificar cada elemento um por um (como na busca linear), a busca binária reduz o problema pela metade a cada passo.
*Eficiência matemática:* A complexidade do algoritmo é expressa por \(O(\log n)\). Isso significa que, em uma lista de 1.000.000 de itens, ela precisará de, no máximo, 20 passos para encontrar o que você procura

# Requisito essencial
Para que a busca binária funcione, a lista DEVE estar ordenada (do menor para o maior, ou vice-versa). Se a lista estiver desordenada, será necessário ordená-la antes de aplicar o algoritmo.

O que fazer quando queremos procurar algo dentro de uma lista? Por exemplo, digamos que você queira encontrar certo número dentro de uma lista:

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Só de olhar, podemos dizer se, por exemplo, o número 4 está dentro dessa lista, ou se temos números pares e/ou ímpares, ou se o número 11 está dentro desta lista. 
No entanto, e quando se trata de listas de inúmeros elementos? Para isso, utilizamos a busca binária.


#  Busca Binária em Python

##  Descrição
Este projeto é uma implementação prática do algoritmo de **Busca Binária** em Python. A busca binária é um algoritmo eficiente para encontrar um item em uma lista ordenada de itens. Ela funciona dividindo repetidamente pela metade o intervalo de busca.

##  Pré-requisitos e Instalação
Para executar este projeto, você precisa ter o Python instalado na sua máquina (versão 3.x recomendada).

1. Clone o repositório (após concluirmos a Fase 3):
   ```bash
   git clone https://github.com/DacompMiniCursos/aula-2-github-e-colabora-o-EduReiss.git
```
2. Navegue até a pasta: 
    ```bash
    cd Busca_Binária
```
 
# Como usar:

Para executar o algoritmo, execute o seguinte comando no terminal:
```bash
python busca_binaria.py
```
E então, nas linhas 18 e 25, mude os parâmetros da função para o elemento que você deseja buscar e a lista em que deseja buscar esse elemento. Após isso, inicie o programa.


# Autor

Desenvolvido pelo calouro Eduardo dos Reis Azevedo como parte do minicurso de Git & GitHub do DACOMP UFMA



## 🎫 Fase 5: Planejamento da Issue
*Draft da primeira Issue que você abrirá no GitHub.*

**Título da Issue:** `feat: Implementar busca binária recursiva`

**Descrição da Issue:**
```text
Atualmente, o algoritmo de busca binária está implementado de forma iterativa (usando laços de repetição). 

**Objetivo:**
- Adicionar uma nova versão do algoritmo utilizando recursividade para fins didáticos.
- Atualizar o README.md explicando a diferença de performance e uso de mem
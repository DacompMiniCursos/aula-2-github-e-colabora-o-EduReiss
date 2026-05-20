'''
# Busca Linear

#[1, 5, 8, 9, 19, 22, 28, 29]
#chave = 20

# Busca Binária

'''
1 - 500
2 - 750
3 - 625
4 - 667
5 - 657
6 - 662
7 - 664
8 - 665
9 - 666


n = 2^c

2^c = n
log 2ˆc = log n

C = log n

l=0
r=5
mid=6
[1, 5, 8, 9, 19, 22, 28, 29]
chave = 10

0. 1. 2. 3. 4. 5. 6. 7
#chave = 25
'''

def binary_search(key, array):
left, right = 0, len(array)-1
whileleft<=right:
mid = left + (right-left)//2
print(left, mid, right)
ifarray[mid]==key:
returnTrue
elifarray[mid]<key:
left = mid+1
#elif array[mid]>key:
else:
right = mid-1
returnFalse

#bissect_left
#bissect_right

print( binary_search(8, [1, 5, 8, 9, 19, 22, 28, 29]) )

[0, 1, 2, 3, 5, 6, 7]
[0, 1, 2]
[0, 1, 2, 3, 4, 5, 6, 8]
[1, 2, 3]

def numero_que_falta(vetor):
 
 
 
[1, 3, 6, 7, 8, 9, 10, 11, 12, 18]
l
r
 
 
for i in range(len(vetor)):
forjinrange(i+1, len(vetor)):
if vetor[i]+vetor[j]==soma:
returnTrue
return False

soma = 15
'''
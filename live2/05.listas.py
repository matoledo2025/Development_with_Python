frutas = ['uva', 'banana', 'maçã', 'laranja', 'abacaxi']
print(frutas)  # ['uva', 'banana', 'maçã', 'laranja', 'abacaxi']

print(frutas[0])  # uva
print(frutas[1])  # banana  
print(frutas[2])  # maçã
print(frutas[3])  # laranja
print(frutas[4])  # abacaxi

frutas.append('melancia')  # adiciona melancia no final da lista
print(frutas)  # ['uva', 'banana', 'maçã', 'laranja', 'abacaxi', 'melancia']

frutas.append('laranja')  # adiciona laranja no final da lista
print(frutas)  # ['uva', 'banana', 'maçã', 'laranja', 'abacaxi', 'melancia', 'laranja']
frutas.pop(1)  # remove o item na posição 1 (banana)


#Listar frutas por frutas
contador = 0
tamanho = len(frutas)
while contador < tamanho:
    #print(frutas[contador])
    #contador += 1
    
    #Adicionando indice nas frutas
    print (f'{contador + 1} - {frutas[contador]}')
    contador += 1
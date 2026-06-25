frutas = ['uva', 'banana', 'maçã', 'laranja', 'abacaxi']

for x in frutas:
    print(x) 
    
#Segundo exemplo
for indice, fruta in enumerate (frutas):
    print(f'{indice + 1} - {fruta}')
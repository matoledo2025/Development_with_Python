nome = input("Digite seu nome: ")
nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))

soma = nota1 + nota2
media = soma / 2



    
#Formas de mstrar ao usuário o resultado
print(f"A soma das notas é: {soma}")
print("A média das notas é:", media)
print(f'{nome} sua média é: {media}')

if media >= 5:

    print(f"{nome} você foi aprovado!")
else:
    print(f"{nome} você foi reprovado!")

#…or create a new repository on the command line
#echo "# Development_with_Python" >> README.md
#git init
#git add README.md
#git commit -m "first commit"
#git branch -M main
#git remote add origin https://github.com/matoledo2025/Development_with_Python.git
#git push -u origin main
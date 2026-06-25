senha_cadastrada = "123456"
senha_digitada = input("Digite sua senha para acessar: ")

while senha_cadastrada != senha_digitada:
    print("Senha incorreta! Tente novamente.")
    senha_digitada = input("Digite sua senha para acessar: ")
    
print("Senha correta! Acesso permitido...")
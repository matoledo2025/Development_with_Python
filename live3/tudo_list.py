import sqlite3

conn = sqlite3.connect('tudo.db')
#conn.row_factory = sqlite3.Row
cursor = conn.cursor()

cursor.execute("""
                   CREATE TABLE IF NOT EXISTS tarefa (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   titulo TEXT NOT NULL,
                   concluida INTEGER DEFAULT 0 
               )
               
               """)
conn.commit()

def adicionar():
    titulo_digitado = input('Digite o titulo da tarefa: ')
    cursor.execute('INSERT INTO tarefa (titulo) VALUES (?)', (titulo_digitado,))
    conn.commit()
    print(f'------------- {titulo_digitado} Cadastrada!!! ---------------')
    
        
def listar():
    cursor.execute('SELECT * FROM tarefa')
    tarefas = cursor.fetchall()
    print('_'*35)
    print(f'Código | Tarefa | Concluído')
    print('_'*35)
    for tarefa in tarefas:
            
        if tarefa [2] == 0:
            status = 'Pendente'  
        else:
            status = 'Concluída'
        #print(f'{tarefa["id"]} | {tarefa["titulo"]} | {tarefa["concluida"]}')
        print(f'{tarefa[0]:<6} |  {tarefa[1]:<10}  | {status}')
        
def concluir():
    listar()
    id_digitado = input ('Escolha um ID da tarefa para concluir: ')
    cursor.execute ('SELECT * FROM tarefa WHERE id = ?', (id_digitado,))
    tarefa = cursor.fetchall()
    print (tarefa)
    
  
       
def menu():
    while True:
        print("\n===== TUDO LIST =====")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Concluir tarefas")
        print("4 - Deletar tarefas")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar()
        elif opcao == '2':
            listar()
        elif opcao == '3':
            concluir()
        elif opcao == '4':
            print("Deletando itens...")
        elif opcao == '0':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente!")

menu()


#VIDEO DA LIVE 3 PAUSDO COM 1:36:23
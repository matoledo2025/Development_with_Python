alunos = [
    {
        'nome': 'Ana',
        'Nota': 8, 
        'uf': 'sp'
    },
    
    {
        'nome': 'Bia', 
        'Nota': 9, 
        'uf': 'rj'
    },
    
    {
        'nome': 'Carlos', 
        'Nota': 7, 
        'uf': 'mg'
    }
]


print(alunos)  # [{'nome': 'Ana', 'Nota': 8, 'uf': 'sp'}, {'nome': 'Bia', 'Nota': 9, 'uf': 'rj'}, {'nome': 'Carlos', 'Nota': 7, 'uf': 'mg'}]

for aluno in alunos:
    print (aluno)  # {'nome': 'Ana', 'Nota': 8, 'uf': 'sp'}, {'nome': 'Bia', 'Nota': 9, 'uf': 'rj'}, {'nome': 'Carlos', 'Nota': 7, 'uf': 'mg'}

print ('#' * 100)
    
alunos.append({'nome': 'Daniel', 'Nota': 10, 'uf': 'sp'})
for aluno in alunos:
    print (aluno)  # {'nome': 'Ana', 'Nota': 8, 'uf': 'sp'}, {'nome': 'Bia', 'Nota': 9, 'uf': 'rj'}, {'nome': 'Carlos', 'Nota': 7, 'uf': 'mg'}
    
    
    
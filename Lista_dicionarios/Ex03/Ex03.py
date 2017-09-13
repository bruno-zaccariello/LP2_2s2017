nome = '_init_'
nota_alunos = {}
while nome != '' :
    nome = str(input('Insira o nome do aluno'))
    if nome == '' :
      break
    nota_alunos[nome] = [float(input('Insira a primeira nota')), float(input('Insira a segunda nota'))]

print(nota_alunos)

nome = str(input('Insira o nome do aluno a buscar'))

def calc_media(name) :
  x = nota_alunos[name]
  media = (x[0] + x[1]) / 2
  return media
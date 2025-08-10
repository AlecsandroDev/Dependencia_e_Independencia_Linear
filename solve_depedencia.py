from string import ascii_letters as alfa
from render_plane import model_geometric 



def print_sistema(list_args: list = []):
  global texto

  for i in list_args:
    for index, l in enumerate(i[:(len(i)-1)]):
      texto += (str(l) + alfa[index] + " ") if l < 0 else "+" + (str(l)+alfa[index] + " ")
    texto += ("= "+ str(i[len(i)-1]) + "\n")


def dependencia_linear(*args: list):
  global texto
  texto = ""

  
  list_args = []
  for i, vector in enumerate(args[0]):
    texto += f"Vetor {alfa[i].upper()} - {(vector[0],vector[1])} \n\n"
    list_args.append([vector[0],vector[1]])
  print(list_args)
  result = []
  line = []

  for i in range(len(list_args[0])):
    for i_line in list_args:
      line.append(i_line[i])
    line.append(0)
    result.append(line)
    line = []

  return resolucao_gauss(result)


def tipo_dependencia(sistema: list):
  global texto

  #if len(sistema[1]) >= 4:
    #texto += "\nSistema com mais de 2 Vetores !\nSPI 'Sistema Possível Indetermindo'\nLD 'Linearmente Dependente'"
    #return texto

  for i, val in enumerate(sistema[1]):
    if i <= 2 and val != 0:
      texto += "\nSPD 'Sistema Possível Determindo'\nLI 'Linearmente Independente'"
      return texto
  else:
      texto += "\nSPI 'Sistema Possível Indetermindo'\nLD 'Linearmente Dependente'"
      return texto

def resolucao_gauss(sistema: list):
  global texto

  list_args = sistema
  line_memory = []
  pivo = None

  texto += "Antes do Metódo de Gauss\n"
  print_sistema(sistema)

  #if len(list_args[1]) >= 4:
    #return tipo_dependencia(list_args)


  if list_args[1][0] != 0:
    for i_line, line in enumerate(list_args[1:]):
      for i_element, element in enumerate(line):
        if element != 0:
          pivo = element / list_args[i_line][i_element]

          for i in list_args[i_line]:  
            line_memory.append(i*pivo)
          break

    
    for i_element, element in enumerate(list_args[1]):
      list_args[1][i_element] -= line_memory[i_element]

    texto += "\nDepois do Metódo de Gauss\n"
    print_sistema(list_args)


  return tipo_dependencia(list_args)
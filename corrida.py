# -*- coding: utf-8 -*-
def calcular_valor_inscricao(distancia,lote,idade):
  """Calcula o valor da inscrição conforme distância, lote e idade."""
  if lote == 1:
     valor = 80.0
  else:
     valor = 100.0

  if distancia == 10:
     valor += 20.0

  if idade >= 60:
     valor = valor / 2

  return valor


def definir_categoria(idade):
  """Retorna a categoria do corredor conforme sua idade."""
  if 16 <= idade < 20:
    return 'Juvenil'
  elif 20 <= idade < 40:
    return 'Adulto'
  elif 40 <= idade < 60:
    return 'Master'
  else:
    return 'Veterano'


def codigo_corredor(nome, idade):
    """Gera o código usando partes do nome e a idade do corredor."""
    nome = nome.strip()

    primeiro_espaco = nome.find(" ")
    ultimo_espaco = nome.rfind(" ")

    if primeiro_espaco == -1:
        primeiro_nome = nome
        ultimo_sobrenome = nome
    else:
        primeiro_nome = nome[:primeiro_espaco]
        ultimo_sobrenome = nome[ultimo_espaco + 1:]

    codigo = (
        primeiro_nome[:3].upper()
        + ultimo_sobrenome[:3].upper()
        + str(idade)
    )

    return codigo


def tempo_para_segundos(tempo):
    """Converte HH:MM:SS em segundos ou retorna -1 se inválido."""
    if len(tempo) != 8:
        return -1

    if tempo[2] != ":" or tempo[5] != ":":
        return -1

    horas = tempo[:2]
    minutos = tempo[3:5]
    segundos = tempo[6:8]

    if not horas.isdigit():
        return -1

    if not minutos.isdigit() or not segundos.isdigit():
        return -1

    horas = int(horas)
    minutos = int(minutos)
    segundos = int(segundos)

    if minutos > 59 or segundos > 59:
        return -1

    return horas * 3600 + minutos * 60 + segundos



def calcular_pace(tempo_segundos, distancia):
"""Calcula o ritmo médio em minutos e segundos por quilômetro."""
 pace_segundos = tempo_segundos // distancia
 minutos = pace_segundos // 60
 segundos  = pace_segundos % 60

 return f"{minutos}'{segundos:02d}\"/km"


def verificar_premiacao(idade, distancia, tempo_segundos):
   """Verifica se o tempo atende ao limite de premiação da categoria."""
   categoria = definir_categoria(idade)
   if distancia == 5:
    if categoria == "Juvenil":
      limite = 25 * 60
    elif categoria == "Adulto":
       limite = 22 * 60
    elif categoria == "Master":
      limite = 25 * 60
    else:
      limite = 30 * 60
   else:
    if categoria == "Juvenil":
      limite = 52 * 60
    elif categoria == "Adulto":
       limite = 46 * 60
    elif categoria == "Master":
       limite = 52 * 60
    else:
       limite = 63 * 60

   return tempo_segundos <= limite



def ler_idade():
    """Solicita uma idade inteira."""
    while True:
        try:
            idade = int(input("Digite sua idade: "))
            return idade
        except ValueError:
            print("Idade inválida. Digite um número inteiro.")


def ler_distancia():
  """Solicita uma distância válida: 5 ou 10 quilômetros."""
  while True:
    try:
      distancia = int(input("Digite a distancia (5 ou 10 km): "))
      if distancia == 5 or distancia == 10:
        return distancia
      print("Distância inválida. Digite apenas 5 ou 10.")
    except ValueError:
      print("Entrada inválida. Digite um número inteiro.")


def ler_lote():
   """Solicita um lote válido: 1 ou 2."""
   while True:
    try:
      lote = int(input("Digite o lote (1 ou 2): "))
      if lote == 1 or lote == 2:
        return lote 
      print('Digite apenas 1 ou 2.')
    except ValueError:
      print("Entrada inválida. Digite um número inteiro.")

def ler_tempo():
   """Solicita um tempo válido no formato HH:MM:SS."""
   while True:
    try:
      tempo = input("Digite seu tempo corrido: (HH: MM: SS): ").strip()
      segundos = tempo_para_segundos(tempo)

      if segundos != -1:
        return tempo,segundos
      
      print("Tempo inválido!")
      print("Utilize o formato HH: MM: SS:")
      print("Exemplo de uso 00: 34: 29")

def fazer_inscricao():
   """Lê os dados do corredor e realiza a inscrição."""
   nome = input("Digite o nome completo: ").strip()

      while len(nome.split()) < 2:
        print("Nome inválido. Digite o nome completo.")
        nome = input("Digite o nome completo: ").strip()

    idade = ler_idade()

    if idade < 16:
        print("Inscrição recusada: idade mínima de 16 anos.")
        return None

    distancia = ler_distancia()
    lote = ler_lote()

    categoria = definir_categoria(idade)
    codigo = codigo_corredor(nome, idade)
    valor = calcular_valor_inscricao(distancia, lote, idade)

    primeiro_espaco = nome.find(" ")
    primeiro_nome = nome[:primeiro_espaco]

      print("_______________ Corrida UNIFSA.26 _______________")
    print("Primeiro nome:", primeiro_nome)
    print("Código do corredor:", codigo)
    print("Categoria:", categoria)
    print("Distância:", distancia, "km")
    print(f"Valor a pagar: R$ {valor:.2f}")
    print("_________________________________________________")

    corredor = {
        "nome": nome,
        "idade": idade,
        "distancia": distancia,
        "lote": lote,
        "codigo": codigo,
        "categoria": categoria,
        "valor": valor,
        "tempo": None
    }

    return corredor


def calcular_resultado():
      """Lê os dados da corrida e exibe o resultado do corredor."""
      idade = ler_idade()

      if idade < 16:
        print("Idade inválida para a corrida. Idade mínima: 16 anos.")
        return

    distancia = ler_distancia()
    tempo, tempo_segundos = ler_tempo()

    categoria = definir_categoria(idade)
    pace = calcular_pace(tempo_segundos, distancia)
    premiacao = verificar_premiacao(
        idade, distancia, tempo_segundos
    )

      print("_______________ Resultado UNIFSA.26 ___________________")
      print("Categoria:",categoria)
      print("Tempo informado",tempo)
      print("Tempo em segundos",tempo_segundos)
      print("Pace",pace)
      if premiacao:
        print("Premiação: SIM ")
      else:
        print("Premiação: NÃO")
      print("_________________________________________________")

def menu():
"""Executa o menu e mantém o resumo das inscrições."""
  quantidade_inscricoes = 0
  total_arrecadado = 0.0

   while True:
        print("\n_______________ Corrida UNIFSA.26 _______________")
        print("1 - Fazer inscrição")
        print("2 - Calcular resultado")
        print("3 - Sair")
        print("_________________________________________________")

        opcao = input("Escolha uma das opções abaixo: ").strip()
        if opcao == "1":    
          valor = fazer_inscricao()

          if valor is not None:
              quantidade_inscricoes += 1
              total_arrecadado += valor

        elif opcao == "2":
            calcular_resultado()

        elif opcao == "3":
            print("\n_______________ Resumo Final ____________________")
            print("Inscrições realizadas:", quantidade_inscricoes)
            print(f"Total arrecadado: R$ {total_arrecadado:.2f}")
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida. Escolha 1, 2 ou 3.")


menu()
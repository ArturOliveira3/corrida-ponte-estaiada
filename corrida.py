# -*- coding: utf-8 -*-
def calcular_valor_inscricao(distancia,lote,idade):

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

  if 16 <= idade < 20:
    return 'Juvenil'
  elif 20 <= idade < 40:
    return 'Adulto'
  elif 40 <= idade < 60:
    return 'Master'
  else:
    return 'Veterano'


def codigo_corredor(nome, idade):
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

 pace_segundos = tempo_segundos // distancia
 minutos = pace_segundos // 60
 segundos  = pace_segundos % 60

 return f"{minutos}'{segundos:02d}\"/km"


def verificar_premiacao(idade, distancia, tempo_segundos):
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
    while True:
        try:
            idade = int(input("Digite sua idade: "))
            return idade
        except ValueError:
            print("Idade inválida. Digite um número inteiro.")


def ler_distancia():
  while True:
    try:
      distancia = int(input("Digite a distancia (5 ou 10 km): "))
      if distancia == 5 or distancia == 10:
        return distancia
      print("Distância inválida. Digite apenas 5 ou 10.")
    except ValueError:
      print("Entrada inválida. Digite um número inteiro.")


def ler_lote():
   while True:
    try:
      lote = int(input("Digite o lote (1 ou 2): "))
      if lote == 1 or lote == 2:
        return lote 
      print('Digite apenas 1 ou 2.')
    except ValueError:
      print("Entrada inválida. Digite um número inteiro.")

def ler_tempo():
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
   while True:
    try:
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

    return valor

def calcular_resultado():
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
  quantidade_inscricoes = 0
  total_arrecadado = 0.00

  while True:
    print('_______________ Corrida UNIFSA.26 ___________________')
    print("1 - Faça sua inscrição aqui")
    print("2 - Calcular resultado")
    print("3 - Sair")
    print('__________________________________')

  opcao = input("Escolha uma das opções abaixo:")
  if opcao == "1"
    valor = fazer_inscricao()

    quantidade_inscricoes += 1
    total_arrecadado += valor
  elif opcao == "2":
    calcular_resultado()

  elif opcao == "3":
    print("Inscrição realizada:", quantidade_inscricoes)
    print("Total arrecadados: R$ ", total_arrecadado)
    print("Sistema Encerrado")


  else:
    print("Opção Inválida! Digite o que estiver dentro do Menu!")
menu()
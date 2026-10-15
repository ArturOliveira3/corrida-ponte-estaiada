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

  if 16 <= idade < 19:
    return 'Juvenil'
  elif 20 <= idade < 39:
    return 'Adulto'
  elif 40 <= idade < 59:
    return 'Master'
  else:
    return 'Veterano'


def codigo_corredor(nome,idade):

 partes = nome.split()

 primeiro_nome = partes[0]
 ultimo_sobrenome = partes[-1]

 codigo = primeiro_nome[:3].upper() + ultimo_sobrenome[:3].upper() + str(idade)

 return codigo_corredor


def tempo_corredor(tempo):

 if (tempo) != 8:
  return -1

 if tempo[2] != ':' or tempo[5] != ':' :
  return -1

 horas = tempo [:2]
 minutos = tempo[3:5]
 segundos = tempo[6:8]
 if not horas.isdigit() or not minutos.isdigit() or not segundos.isdigit():
  return -1

  horas = int(horas)
  minutos= int(minutos)
  segundos = int(segundos)

  if minutos > 59 or sgundos > 59:
    return -1

 return horas * 3600 + minutos * 60 + segundos



def calcular_pace(tempo_segundos, distancia):

 pace_segundos = tempo_segundos // distancia
 minutos = pace_segundos // 60
 segundo = pace_segundos % 60

 return f"{minutos}'{segundos:02d}\"/km"


def verificar_premiacao(idade, distancia, tempo_segundo):
   categoria = definir_categoria(idade)
   if distancia == 5:
    if categoria == "Juvenil":
      limiete = 25 * 60
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

   return tempo_segundo <= limite



def ler_idade():
    while True:
        try:
          idade = int(input("Digite sua idade:"))

          if idade >= 16:
            return idade
            print("A idade mímina é 16 anos.")
          else:
            print("Idade inválida.Digite a distância certa!")


def ler_distancia():
  while True:
    try:
      distancia = int(input("Digite a distancia (5 ou 10 km:)"))
      if distancia == 5 or distancia == 10:
        return distancia
        print("Digite apenas 5 ou 10.")
      else:
        print("Distância inválida. Digite a distância certa!")


def ler_lote():
   while True:
    try:
      lote = int(input("Digite o lote (1 ou 2):"))
      if lote == 1 or lote == 2:
        return lote
        print('Digite apenas 1 ou 2.')
      else:
        print("Lote inválido. Digite o lote certo!")

def ler_tempo():
   while True:
    try:
      tempo = int(input("Digite seu tempo corrido: (HH: MM: SS):"))

      segundos = tempo_para_segundos(tempo)
      if segundos != -1:
        return tempo,segundos
      print("Tempo inválido!")
      print("Use o forma sugerido HH: MM: SS:")
      print("Exemplo de uso 00: 34: 29")

def fazer_inscricao():
   while True:
    try:
      nome = int(input("Digite o nome completo:"))
      idade = ler_idade
      categoria = definir_categoria
      lote = ler_lote
      distancia = ler_distancia
      codigo = codigo_corredor
      valor = calcular_valor_inscricao(distancia, lote, idade)

      primeiro_nome = nome.split()[0]

      print('_______________ Corrida UNIFSA.26 ___________________')
      print("Digite seu Primeiro nome:",primeiro_nome)
      print('Código do corredor',codigo)
      print('Categoria ',categoria)
      print('Distancia',distancia)
      print("Valor a pagar: R$ ", valor)
      print('__________________________________')
      return valor

def calculr_resultado():
      idade = ler_idade()
      distancia = ler_distancia()

      tempo,tempo_segundo = ler_tempo()

      categoria = definir_categoria(idade)
      pace = calcular_pace(tempo_segundos, distancia)
      premiacao = verificar_premiacao(idade, distancia, tempo_segundo)

      print('_______________ Resultado UNIFSA.26 ___________________')
      print("Categoria:",categoria)
      print("Tempo informado",tempo)
      print("Tempo em segundos",tempo_segundo)
      print("Pace",pace)
      if premiado:
        print("Pemiação: SIM ")
      else:
        print("PRemiação: NÃO")
      print('__________________________________')

def menu():
  quantidade_inscricoes = 0
  total_arreacado = 0.00

  while True:
    print('_______________ Corrida UNIFSA.26 ___________________')
    print("1 - Faça sua escrição aqui")
    print("2 - Calcular resultado")
    print("3 - Sair")
    print('__________________________________')

  opcao = input("Escolha uma das opções abaixo:")
  if opcao == "1"
    valor = fazer_inscricao()

    quantidade_inscricoes += 1
    total_arreacado += valor
  elif opcao == "2":
    calcular_resultado()

  elif opcao == "3":
    print("Inscrição realizada:", quantidade_inscricoes)
    print("Total arrecadados: R$ ", total_arreacado)
    print("Sistema Encerrado")


  else:
    print("Opção Inválida! Digite o que estiver dentro do Menu!")
menu()
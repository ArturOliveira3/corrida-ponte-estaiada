# -*- coding: utf-8 -*-
TEMPOS_LIMITE = (
    ("Juvenil", 25 * 60, 52 * 60),
    ("Adulto", 22 * 60, 46 * 60),
    ("Master", 25 * 60, 52 * 60),
    ("Veterano", 30 * 60, 63 * 60),
)


CODIGOS_UTILIZADOS = set()


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
     """Gera um código único para o corredor."""
     partes_nome = nome.strip().split()
     primeiro_nome = partes_nome[0]
     sobrenome = partes_nome[-1]

     codigo_base = (
        primeiro_nome[:3] + sobrenome[:3] + str(idade)
    ).upper()

     codigo = codigo_base
     contador = 1

     while codigo in CODIGOS_UTILIZADOS:
        codigo = f"{codigo_base}{contador}"
        contador += 1

     CODIGOS_UTILIZADOS.add(codigo)
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
   
   for nome_categoria, limite_5km, limite_10km in TEMPOS_LIMITE:
        if nome_categoria == categoria:
            if distancia == 5:
                limite = limite_5km
            else:
                limite = limite_10km

            return tempo_segundos <= limite

   return False



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

def listar_inscritos(corredores):
    """Exibe os dados de todos os corredores cadastrados."""
    if len(corredores) == 0:
        print("Nenhum corredor cadastrado.")
        return

    for corredor in corredores:
        print("------------------------------")
        print("Nome:", corredor["nome"])
        print("Idade:", corredor["idade"])
        print("Distância:", corredor["distancia"], "km")
        print("Lote:", corredor["lote"])
        print("Código:", corredor["codigo"])
        print("Categoria:", corredor["categoria"])
        print(f"Valor: R$ {corredor['valor']:.2f}")

        if corredor["tempo"] is None:
            print("Tempo: Não registrado")
        else:
            print("Tempo:", corredor["tempo"])

    print("------------------------------")


def contar_por_categoria(corredores):
    """Exibe a quantidade de corredores inscritos em cada categoria."""
    categorias = {}

    for corredor in corredores:
        categoria = corredor["categoria"]
        categorias[categoria] = categorias.get(categoria, 0) + 1

    for categoria, quantidade in categorias.items():
        print(f"{categoria}: {quantidade} inscrito(s)")


def listar_corredores_com_tempo(corredores):
    """Retorna os corredores que possuem tempo registrado."""
    return [
        corredor for corredor in corredores
        if corredor["tempo"] is not None
    ]


def listar_corredores_premiados(corredores):
    """Retorna os corredores que atendem aos critérios de premiação."""
    return [
        corredor for corredor in corredores
        if corredor["tempo"] is not None
        and verificar_premiacao(
            corredor["idade"],
            corredor["distancia"],
            tempo_para_segundos(corredor["tempo"])
        )
    ]


def classificar_corredores(corredores, distancia):
    """Exibe a classificação geral dos corredores por distância."""
    classificados = [
        corredor for corredor in corredores
        if corredor["distancia"] == distancia
        and corredor["tempo"] is not None
    ]

    classificados.sort(
        key=lambda corredor: tempo_para_segundos(corredor["tempo"])
    )

    print(f"\nClassificação geral - {distancia} km")

    if not classificados:
        print("Nenhum corredor possui tempo registrado nessa distância.")
        return

    for posicao, corredor in enumerate(classificados, start=1):
        print(
            f"{posicao}º lugar: {corredor['nome']} - "
            f"{corredor['tempo']}"
        )


def buscar_corredor(corredores, codigo):
     """Retorna o corredor correspondente ao código ou None se não existir."""
     for corredor in corredores:
        if corredor["codigo"] == codigo:
            return corredor

     return None

def registrar_tempo(corredores, codigo, tempo):
     """Registra o tempo de prova de um corredor cadastrado."""
     corredor = buscar_corredor(corredores, codigo)

     if corredor is None:
        return False

     corredor["tempo"] = tempo
     return True


def menu():
    """Executa o menu e mantém o resumo das inscrições."""
    corredores = []
    quantidade_inscricoes = 0
    total_arrecadado = 0.0

    while True:
        print("\n_______________ Corrida UNIFSA.26 _______________")
        print("1 - Cadastrar corredor")
        print("2 - Listar inscritos")
        print("3 - Buscar corredor pelo código")
        print("4 - Registrar tempo de prova")
        print("5 - Contagem por categoria")
        print("6 - Sair")
        print("_________________________________________________")

        opcao = input("Escolha uma das opções abaixo: ").strip()
        if opcao == "1":    
          corredor = fazer_inscricao()

          if corredor is not None:
              corredores.append(corredor)
              quantidade_inscricoes += 1
              total_arrecadado += corredor["valor"]

        elif opcao == "2":
            listar_inscritos(corredores)

        elif opcao == "3":
            codigo = input("Digite o código do corredor: ").strip().upper()
            corredor = buscar_corredor(corredores, codigo)

            if corredor is not None:
                print("------------------------------")
                print("Nome:", corredor["nome"])
                print("Idade:", corredor["idade"])
                print("Distância:", corredor["distancia"], "km")
                print("Lote:", corredor["lote"])
                print("Código:", corredor["codigo"])
                print("Categoria:", corredor["categoria"])
                print(f"Valor: R$ {corredor['valor']:.2f}")

                if corredor["tempo"] is None:
                    print("Tempo: Não registrado")
                else:
                    print("Tempo:", corredor["tempo"])

                print("------------------------------")
            else:
                print("Corredor não encontrado.")

        elif opcao == "4":
            codigo = input("Digite o código do corredor: ").strip().upper()
            tempo = None

            corredor = buscar_corredor(corredores, codigo)

            if corredor is None:
                print("Corredor não encontrado.")
            else:
                tempo, tempo_segundos = ler_tempo()

                if registrar_tempo(corredores, codigo, tempo):
                    categoria = corredor["categoria"]
                    distancia = corredor["distancia"]
                    pace = calcular_pace(tempo_segundos, distancia)
                    premiacao = verificar_premiacao(
                        corredor["idade"],
                        distancia,
                        tempo_segundos
                    )

                    print("Tempo registrado com sucesso.")
                    print("Corredor:", corredor["nome"])
                    print("Categoria:", categoria)
                    print("Tempo:", tempo)
                    print("Tempo em segundos:", tempo_segundos)
                    print("Pace:", pace)
                    print("Premiação:", "SIM" if premiacao else "NÃO")


        elif opcao == "5":
            contar_por_categoria(corredores)

        elif opcao == "6":
            print("\n_______________ Resumo Final ____________________")
            print("Inscrições realizadas:", quantidade_inscricoes)
            print(f"Total arrecadado: R$ {total_arrecadado:.2f}")
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida. Escolha de 1 a 6.")


menu()
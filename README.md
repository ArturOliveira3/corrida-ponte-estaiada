# 🏃 Corrida Noturna da Ponte Estaiada

Sistema de inscrições e resultados da Corrida Noturna da Ponte Estaiada, desenvolvido em Python para a disciplina de Programação I do UNIFSA.

O projeto tem como objetivo gerenciar as inscrições dos participantes e organizar os resultados da corrida, conforme os requisitos estabelecidos nas etapas do trabalho.

## 📋 Requisitos

- Python 3.x instalado.
- Editor de código, como Visual Studio Code(Vscode), e uso de Google Colab.


**Observação:** dependendo da instalação, pode ser necessário utilizar o comando `python3 corrida.py`.

## ⚙️ Funcionalidades

### Etapa 1 — Funcionalidades básicas

- Comando para fazer inscrição do corredor:
  ``` text 
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

- Comando para calcular resultado do corredor:
  ``` text
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

    print("_______________ Resultado UNIFSA.26 _______________")
    print("Categoria:", categoria)
    print("Tempo informado:", tempo)
    print("Tempo em segundos:", tempo_segundos)
    print("Pace:", pace)

    if premiacao:
        print("Premiação: SIM")
    else:
        print("Premiação: NÃO")

    print("___________________________________________________")

- Comando para sair + resultado esperado:
 ``` text 
  _______________ Corrida UNIFSA.26 _______________
1 - Fazer inscrição
2 - Calcular resultado
3 - Sair
_________________________________________________
Escolha uma opções abaixos: 1
Digite o nome completo:Diego Soares Leandro
Digite sua idade: 23
Digite o lote (1 ou 2): 1
Digite a distância (5 ou 10 km): 5
```
### Etapa 2 — Funcionalidades e níveis implementados

- **Nível 1: Essencial:**
``` text
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

---------------------------------------------------
def contar_por_categoria(corredores):
    """Exibe a quantidade de corredores inscritos em cada categoria."""
    categorias = {}

    for corredor in corredores:
        categoria = corredor["categoria"]
        categorias[categoria] = categorias.get(categoria, 0) + 1

    for categoria, quantidade in categorias.items():
        print(f"{categoria}: {quantidade} inscrito(s)")

---------------------------------------------
def listar_corredores_com_tempo(corredores):
    """Retorna os corredores que possuem tempo registrado."""
    return [
        corredor for corredor in corredores
        if corredor["tempo"] is not None
    ]

------------------------------------
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

-----------------------------------------------------
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

```
- **Nível 2: Intermediário:**
``` text
def gerar_relatorio_final(corredores):
    """Exibe estatísticas finais das provas de 5 km e 10 km."""
    print("\n_______________ Relatório Final _______________")

    for distancia in (5, 10):
        classificados = [
            corredor for corredor in corredores
            if corredor["distancia"] == distancia
            and corredor["tempo"] is not None
        ]

        print(f"\nProva de {distancia} km:")

        if not classificados:
            print("Nenhum tempo registrado.")
            continue

        tempos = [
            tempo_para_segundos(corredor["tempo"])
            for corredor in classificados
        ]

        media = sum(tempos) / len(tempos)
        mais_rapido = min(
            classificados,
            key=lambda corredor: tempo_para_segundos(corredor["tempo"])
        )

        print(f"Tempo médio: {media:.2f} segundos")
        print(
            f"Corredor mais rápido: {mais_rapido['nome']} "
            f"({mais_rapido['tempo']})"
        )
```

- **Nível 3: Avançado + resultado esperado :**
``` text
def exibir_podio(corredores, distancia):
    """Exibe os três melhores corredores de cada categoria e distância."""
    categorias = ("Juvenil", "Adulto", "Master", "Veterano")

    for categoria in categorias:
        classificados = [
            corredor for corredor in corredores
            if corredor["categoria"] == categoria
            and corredor["distancia"] == distancia
            and corredor["tempo"] is not None
        ]

        classificados.sort(
            key=lambda corredor: tempo_para_segundos(corredor["tempo"])
        )

        print(f"\nPódio {categoria} - {distancia} km")

        if not classificados:
            print("Nenhum corredor com tempo registrado.")
            continue

        for posicao, corredor in enumerate(classificados[:3], start=1):
            print(
                f"{posicao}º lugar: {corredor['nome']} - "
                f"{corredor['tempo']}"
            )
-----------------------------------------------
  def exibir_podio(corredores, distancia):
    """Exibe os três melhores corredores de cada categoria e distância."""
    categorias = ("Juvenil", "Adulto", "Master", "Veterano")

    for categoria in categorias:
        classificados = [
            corredor for corredor in corredores
            if corredor["categoria"] == categoria
            and corredor["distancia"] == distancia
            and corredor["tempo"] is not None
        ]

        classificados.sort(
            key=lambda corredor: tempo_para_segundos(corredor["tempo"])
        )

        print(f"\nPódio {categoria} - {distancia} km")

        if not classificados:
            print("Nenhum corredor com tempo registrado.")
            continue

        for posicao, corredor in enumerate(classificados[:3], start=1):
            print(
                f"{posicao}º lugar: {corredor['nome']} - "
                f"{corredor['tempo']}"
            )
-----------------------------------
def gerar_relatorio_final(corredores):
    """Exibe estatísticas finais das provas de 5 km e 10 km."""
    print("\n_______________ Relatório Final _______________")

    for distancia in (5, 10):
        classificados = [
            corredor for corredor in corredores
            if corredor["distancia"] == distancia
            and corredor["tempo"] is not None
        ]

        print(f"\nProva de {distancia} km:")

        if not classificados:
            print("Nenhum tempo registrado.")
            continue

        tempos = [
            tempo_para_segundos(corredor["tempo"])
            for corredor in classificados
        ]

        media = sum(tempos) / len(tempos)
        mais_rapido = min(
            classificados,
            key=lambda corredor: tempo_para_segundos(corredor["tempo"])
        )

        print(f"Tempo médio: {media:.2f} segundos")
        print(
            f"Corredor mais rápido: {mais_rapido['nome']} "
            f"({mais_rapido['tempo']})"
        )
---------------------------------------------------------------
def buscar_corredor(corredores, codigo):
     """Retorna o corredor correspondente ao código ou None se não existir."""
     for corredor in corredores:
        if corredor["codigo"] == codigo:
            return corredor

     return None
-----------------------------------------
def registrar_tempo(corredores, codigo, tempo):
     """Registra o tempo de prova de um corredor cadastrado."""
     corredor = buscar_corredor(corredores, codigo)

     if corredor is None:
        return False

     corredor["tempo"] = tempo
     return True

          
```
💻 Exemplo de uso
``` Text
_______________ Corrida UNIFSA.26 _______________
1 - Cadastrar corredor
2 - Listar inscritos
3 - Buscar corredor pelo código
4 - Registrar tempo de prova
5 - Contagem por categoria
6 - Classificação geral
7 - Pódio por categoria
8 - Sair
_________________________________________________
Escolha uma das opções abaixo: 1
Digite o nome completo: Leila Yuka Caiado
Digite sua idade: 56
Digite a distancia (5 ou 10 km): 5
Digite o lote (1 ou 2): 1

-------------------------------------------------
_______________ Corrida UNIFSA.26 _______________
Primeiro nome: Leila
Código do corredor: LEICAI56
Categoria: Master
Distância: 5 km
Valor a pagar: R$ 80.00
_________________________________________________


_______________ Corrida UNIFSA.26 _______________
1 - Cadastrar corredor
2 - Listar inscritos
3 - Buscar corredor pelo código
4 - Registrar tempo de prova
5 - Contagem por categoria
6 - Classificação geral
7 - Pódio por categoria
8 - Sair
_________________________________________________
Escolha uma das opções abaixo: 2
------------------------------
Nome: Leila Yuka Caiado
Idade: 56
Distância: 5 km
Lote: 1
Código: LEICAI56
Categoria: Master
Valor: R$ 80.00
Tempo: Não registrado
------------------------------


_______________ Corrida UNIFSA.26 _______________
1 - Cadastrar corredor
2 - Listar inscritos
3 - Buscar corredor pelo código
4 - Registrar tempo de prova
5 - Contagem por categoria
6 - Classificação geral
7 - Pódio por categoria
8 - Sair
_________________________________________________
Escolha uma das opções abaixo: 3
Digite o código do corredor: LEICAI56
------------------------------
Nome: Leila Yuka Caiado
Idade: 56
Distância: 5 km
Lote: 1
Código: LEICAI56
Categoria: Master
Valor: R$ 80.00
Tempo: Não registrado
------------------------------


_______________ Corrida UNIFSA.26 _______________
1 - Cadastrar corredor
2 - Listar inscritos
3 - Buscar corredor pelo código
4 - Registrar tempo de prova
5 - Contagem por categoria
6 - Classificação geral
7 - Pódio por categoria
8 - Sair
_________________________________________________
Escolha uma das opções abaixo: 4
Digite o código do corredor: LEICAI56
Digite seu tempo corrido: (HH: MM: SS): 02:47:28
Tempo registrado com sucesso.
Corredor: Leila Yuka Caiado
Categoria: Master
Tempo: 02:47:28
Tempo em segundos: 10048
Pace: 33'29"/km
Premiação: NÃO


_______________ Corrida UNIFSA.26 _______________
1 - Cadastrar corredor
2 - Listar inscritos
3 - Buscar corredor pelo código
4 - Registrar tempo de prova
5 - Contagem por categoria
6 - Classificação geral
7 - Pódio por categoria
8 - Sair
_________________________________________________
Escolha uma das opções abaixo: 5
Master: 1 inscrito(s)


_______________ Corrida UNIFSA.26 _______________
1 - Cadastrar corredor
2 - Listar inscritos
3 - Buscar corredor pelo código
4 - Registrar tempo de prova
5 - Contagem por categoria
6 - Classificação geral
7 - Pódio por categoria
8 - Sair
_________________________________________________
Escolha uma das opções abaixo: 6
Escolha a distância (5 ou 10 km): 5

Classificação geral - 5 km
1º lugar: Leila Yuka Caiado - 02:47:28


_______________ Corrida UNIFSA.26 _______________
1 - Cadastrar corredor
2 - Listar inscritos
3 - Buscar corredor pelo código
4 - Registrar tempo de prova
5 - Contagem por categoria
6 - Classificação geral
7 - Pódio por categoria
8 - Sair
_________________________________________________
Escolha uma das opções abaixo: 7
Escolha a distância (5 ou 10 km): 5

Pódio Juvenil - 5 km
Nenhum corredor com tempo registrado.

Pódio Adulto - 5 km
Nenhum corredor com tempo registrado.

Pódio Master - 5 km
1º lugar: Leila Yuka Caiado - 02:47:28

Pódio Veterano - 5 km
Nenhum corredor com tempo registrado.


_______________ Corrida UNIFSA.26 _______________
1 - Cadastrar corredor
2 - Listar inscritos
3 - Buscar corredor pelo código
4 - Registrar tempo de prova
5 - Contagem por categoria
6 - Classificação geral
7 - Pódio por categoria
8 - Sair
_________________________________________________
Escolha uma das opções abaixo: 8


_______________ Relatório Final _______________

Prova de 5 km:
Tempo médio: 10048.00 segundos
Corredor mais rápido: Leila Yuka Caiado (02:47:28)

Prova de 10 km:
Nenhum tempo registrado.


_______________ Resumo Final ____________________
Inscrições realizadas: 1
Total arrecadado: R$ 80.00
Sistema encerrado.
Colab paid products

```

## 🧠 Decisões da dupla

Durante o desenvolvimento do projeto, foram tomadas decisões para organizar o código e facilitar sua manutenção.

- **Organização do código:** Primeiro fezimos as primeiras construções no código pelo Google Colab, assim a dupla conseguia visualizar o desenvolvimento de ambos configurando conforme as exigencias do professor no trabalho
- **Reutilização de código:** Para mais aprimoramento do trabalho utilizamos o Vscode e juntar as partes que foram divididas pela dupla, no fim juntamos para alinhamos o corpo final do trabalho para a entrega 

## 👥 Autores

- **Leticia de O.S Leandro:** https://github.com/MusMus19Leh
- **Arthur O.S Pereira:** https://github.com/ArturOliveira3

---

Projeto acadêmico desenvolvido para a disciplina de Programação I — UNIFSA.

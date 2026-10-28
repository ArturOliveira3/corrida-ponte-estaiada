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
```
- **Nível 2: Intermediário:**
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

```
- **Nível 3: Avançado + resultado esperado :**
``` text
_______________ Corrida UNIFSA.26 _______________
1 - Cadastrar corredor
2 - Listar inscritos
3 - Buscar corredor pelo código
4 - Registrar tempo de prova
5 - Sair
_________________________________________________

Escolha uma opção: 1
Digite o nome completo: Leila Leão Carvalho 
Digite sua idade: 34
Digite a distância (5 ou 10 km): 5
Digite o lote (1 ou 2): 1

_______________ Corrida UNIFSA.26 _______________

Primeiro nome: Leila
Código do corredor: LEICAR34
Categoria: Adulto
Distância: 5 km
Valor a pagar: R$ 80.00

_________________________________________________

Escolha uma opção: 2
------------------------------
Nome: Leila Leão Carvalho
Idade: 34
Distância: 5 km
Lote: 1
Código: LEICAR34
Categoria: Adulto
Valor: R$ 80.00
Tempo: Não registrado


```
💻 Exemplo de uso



## 🧠 Decisões da dupla

Durante o desenvolvimento do projeto, foram tomadas decisões para organizar o código e facilitar sua manutenção.

- **Organização do código:** Letícia fez as primeiras construções no código pelo Google Colab, assim a dupla conseguia visualizar o desenvolvimento de ambos os integrantes 
- **Reutilização de código:** Para mais aprimoramento do trabalho utilizamos o Vscode e juntar as partes que foram divididas em ambos os grupos, no fim juntar para formar o corpo final do trabalho 

## 👥 Autores

- **Leticia de O.S Leandro:** https://github.com/MusMus19Leh
- **Arthur:** https://github.com/ArturOliveira3

---

Projeto acadêmico desenvolvido para a disciplina de Programação I — UNIFSA.

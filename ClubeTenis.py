## ---------------------------- INICIAÇÃO DAS LISTAS ----------------------------
nomes = ["Kim Wexler", "Walter White", "Jesse Pinkman", "Gustavo Fring", "Saul Goodman", "Jane Margolis"]
generos = ["F", "M", "M", "M", "M", "F"]
nacionalidades = ["Estadounidense", "Estadounidense", "Estadounidense", "Chileno", "Estadounidense", "Estadounidense"]
escaloes = ["Master", "Master", "Sénior", "Master", "Master", "Sénior"]
estilos = ["versátil", "ofensivo", "defensivo", "ofensivo", "defensivo", "versátil"]
idades = [39, 50, 25, 48, 41, 24]
alturas = [1.67, 1.78, 1.77, 1.81, 1.80, 1.71]
pesos = [46.1, 72.3, 56.2, 60.1, 68.4, 52.5]
imc = [16.3, 22.7, 17.9, 18.3, 21, 17.8]

# ----------------------------INSERSÃO DE UM NOVO ATLETA ----------------------------
def inserir():
    print("INSERIR NOV@ ATLETA")
    nome = input("Nome: ")
    gen = input("Genero (M/F): ")
    nac = input("Nacionalidade: ")
    esc = input("Escalao (de idade): ")
    est = input("Estilo (ofensivo/defensivo/versátil): ")
    idade = input("Idade: ")
    h = input("Altura (m): ")
    peso = input("Peso (kg): ")

    nomes.append(nome)
    generos.append(gen)
    nacionalidades.append(nac)
    escaloes.append(esc)
    estilos.append(est)
    idades.append(idade)
    alturas.append(h)
    pesos.append(peso)

    print("Dados inseridos com sucesso!")
#----------------------------ELIMINAR DADOS DOS ATLETAS------------------------
def eliminar():
    input()
#----------------------------CONSULTAR DADOS DE UM ATLETA------------------------
def consultar():
    input()
#----------------------------LISTAR DADOS DOS ATLETAS------------------------
def listar():
    print("\n(Nome) - (Genero) - (Nacionalidade) - (Escalao) - (Estilo)")
    for i in range(len(nomes)):
        print(f"{nomes[i]} - {generos[i]} - {nacionalidades[i]} - {escaloes[i]} - {estilos[i]}")
    print("\n")
    print("Oprima qualquer tecla para continuar")
    input()

#---------------------------ESTATISTICAS DO ATLETA---------------------------
def estatisticas():
    print("\n(Nome) - (Idade) - (Altura) - (Peso) - (IMC)")
    for i in range(len(nomes)):
        print(f"{nomes[i]} - {idades[i]} - {alturas[i]} - {pesos[i]} - {imc[i]}")
    print("\n")
    print("Oprima qualquer tecla para continuar")
    input()
# ---------------------------- MENÚ PRINCIPAL ----------------------------
print("GESTAO DE ATLETAS DO CLUBE DE TENIS")
while True:
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Inserir atleta e respetivos dados. ")
    print("2. Eliminação atleta e respetivos dados. ")
    print("3. Consultação de dados. ")
    print("4. Listagem de dados. ")
    print("5. Estatísticas. ")
    print("0. Sair. ")

    opcao = input("Selecione uma opção: ")
    if opcao == "1":
        inserir()
    elif opcao == "2":
        eliminar()
    elif opcao == "3":
        consultar()
    elif opcao == "4":
        listar()
    elif opcao == "5":
        estatisticas()
    elif opcao == "0":
        print("Encerrando o programa. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")
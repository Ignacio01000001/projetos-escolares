# Listas iniciais
distritos = ["Aveiro", "Beja", "Braga", "Bragança", "Castelo Branco", "Coimbra", "Évora", "Faro", "Guarda", "Leiria",
             "Lisboa", "Portalegre", "Porto", "Santarém", "Setúbal"]
tempMax = [11, 13, 15, 17, 20, 24, 26, 28, 23, 18, 14, 11, 16, 18, 20]
tempMin = [2, 3, 4, 6, 8, 11, 13, 13, 11, 8, 5, 3, 7, 5, 6]
ampTerm = [9, 10, 11, 9, 12, 13, 13, 15, 12, 10, 9, 8, 6, 13, 14]
precipitacao = [5, 0, 20, 15, 0, 10, 0, 0, 10, 5, 0, 12, 0, 0, 5]

# Função para inserir um novo distrito
def inserir():
    print("\nINSERIR NOVO DISTRITO")
    dis = input("Nome do distrito: ")
    tmax = int(input("Temperatura máxima: "))
    tmin = int(input("Temperatura mínima: "))
    pr = int(input("Precipitação: "))

    distritos.append(dis)
    tempMax.append(tmax)
    tempMin.append(tmin)
    ampTerm.append(tmax - tmin)
    precipitacao.append(pr)

    print("\nDados inseridos com sucesso!\n")
    listar()

# Função para listar os dados
def listar():
    print("\nDISTRITO - TEMP. MAX - TEMP. MIN - AMPLITUDE - PRECIPITAÇÃO")
    for i in range(len(distritos)):
        print(f"{distritos[i]} - {tempMax[i]} - {tempMin[i]} - {ampTerm[i]} - {precipitacao[i]}")
    print("\n")
    print("Oprima qualquer tecla para continuar")
    input()

# Função para eliminar um distrito
def eliminar():
    print("\nELIMINAR UM DISTRITO")
    dis = input("Digite o nome do distrito a eliminar: ")

    if dis in distritos:
        idx = distritos.index(dis)
        distritos.pop(idx)
        tempMax.pop(idx)
        tempMin.pop(idx)
        ampTerm.pop(idx)
        precipitacao.pop(idx)
        print(f"\nDistrito '{dis}' eliminado com sucesso!\n")
    else:
        print(f"\nDistrito '{dis}' não encontrado.\n")
    listar()

# Programa principal
print("GESTÃO DE DADOS CLIMÁTICOS")
while True:
    print("1 - Inserir dados")
    print("2 - Eliminar dados")
    print("3 - Listar dados")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        inserir()
    elif opcao == "2":
        eliminar()
    elif opcao == "3":
        listar()
    elif opcao == "0":
        print("Encerrando o programa. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")
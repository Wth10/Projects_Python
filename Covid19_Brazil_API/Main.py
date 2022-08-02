import os
import database

O = 0


def Menu():
    global O
    print("### Covid19 Brazil API ###\n")
    print("[1] Lista Casos Por Todos Estados Brasileiros")
    print("[2] Lista Casos Por Estado Brasileiro")
    print("[3] Lista Casos No Brasil Em Data Específica")
    print("[4] Consultar Status Da API")
    print("[5] Sair \n")

    O = int(input("Digite a opção desejada: "))


while O != 5:
    os.system("cls")
    Menu()

    if O == 1:
        os.system("cls")
        print("### Listar Todos Os Cassos ###\n")
        list_all = database.getAll()
        UFs = list_all["data"]
        print("UF  | Cidade | Casos |  Mortes")

        for uf in UFs:
            print(f"{uf['uf']} - {uf['state']} - {uf['cases']} - {uf['deaths']}")

    elif O == 2:
        os.system("cls")
        print("### Listar Casos Por Estados ###\n")
        uf = input("Digite Um Estado: ")
        state = database.getUf(uf)
        print("")
        for key, value in state.items():
            print(f"{key}: {value}")

    elif O == 3:
        os.system("cls")
        print("### Listar Casos Por Data Específica ###\n")
        day = input("Digite Um Dia: ")
        month = input("Digite Um Mês: ")
        year = input("Digite Um Ano: ")
        print("")
        date = year + month + day

        data = database.getDate(date)
        formatted_date = data["data"]

        for x in formatted_date:
            print(f"{x['uf']} - {x['state']} - {x['cases']} - {x['deaths']}")

    elif O == 4:
        os.system("cls")
        print("### Status Da API ###\n")
        print("200 OK")

    input("\nAperte 'ENTER' Para Continuar\n")

print("\nOBRIGADO POR USAR O SISTEMA🥳\n")

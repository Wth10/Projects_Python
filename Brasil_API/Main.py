import os
import database

O = 0


def Banks():
    os.system("cls")
    list_banks = database.getBanks()
    list_banks.sort(key=lambda x: x.name)

    for x in list_banks:
        x.print()
    print("")
    print("Total De Banco Encontrados: ", len(list_banks))


def CEP():
    os.system("cls")
    print("##### | Busca Pelo CEP | ##### \n")
    CEP = input("Digite Um CEP: ")
    list_CEP = database.getCEP(CEP)
    print("")

    for key, value in list_CEP.items():
        print(f"{key} | {value}")


def CNPJ():
    os.system("cls")
    ("##### | Busca CNPJ | #####")
    CNPJ = input("Digite Um CNPJ: ")
    list_CNPJ = database.getCNPJ(CNPJ)

    for key, value in list_CNPJ.items():
        print(f"{key} : {value}")


def DDD():
    os.system("cls")
    print("##### | Listar Cidades Pelo DDD | #####")
    DDD = input("Digite o DDD: ")
    list_DDD = database.getDDD(DDD)
    print("")

    for value in list_DDD["cities"]:
        print(value)
    print("")
    print(f"Cidades  |  Estado: {list_DDD['state']}\n")


def Holidays():
    os.system("cls")
    print(" ##### | Listar Feriados Nacionais Em Determinado Ano | #####")
    Year = input("Digite o ano: ")
    list_Year = database.getHolidays(Year)

    print("________________________________________")
    for x in list_Year:
        print(f"Nome: {x['name']}")
        print(f"Data: {x['date']} - Tipo: {x['type']}")
        print("________________________________________")


def Menu():
    global O
    os.system("cls")
    print("### Brasil API ###\n")
    print("[1] Lista Todos Os Bancos Do Brasil")
    print("[2] Busca Por CEP")
    print("[3] Busca Por CNPJ")
    print("[4] Lista Cidades Por DDD")
    print("[5] Lista Feriados")
    print("[6] Sair \n")

    O = int(input("Digite a opção desejada: "))


while O != 6:
    Menu()

    if O == 1:
        Banks()
    if O == 2:
        CEP()
    if O == 3:
        CNPJ()
    if O == 4:
        DDD()
    if O == 5:
        Holidays()

    input("\nAperte 'ENTER' Para Continuar\n")
    os.system("cls")
print("\nOBRIGADO POR USAR O SISTEMA🥳\n")

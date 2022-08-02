import os
import pyautogui

from model.Employee.Employee import Employee
import model.Employee.Employee_dao as ObjEmployee

from model.Sales.Sales import Sales
import model.Sales.Sales_dao as ObjSales

from model.Dish.Dish import Dish
import model.Dish.Dish_dao as ObjDish

O = 0
# Criar Funcionário
D1 = Employee("João", "Gerente")
D2 = Employee("Mariona", "Recepcionista")
D3 = Employee("Bianca", "Serviços Gerais")
D4 = Employee("Pedro", "Recepcionista")

# Adicionndo Funcionário
ObjEmployee.Add(D1)
ObjEmployee.Add(D2)
ObjEmployee.Add(D3)
ObjEmployee.Add(D4)

# Criar Prato
D1 = Dish("Pizza Pequena", "Ótima", 35)
D2 = Dish("Pizza Grande", "Ótima", 45)
D3 = Dish("Pastel", "Frango", 4)
D4 = Dish("Suco", "Fruta", 2)

# Adicionndo Prato
ObjDish.Add(D1)
ObjDish.Add(D2)
ObjDish.Add(D3)
ObjDish.Add(D4)


def Main_Menu():
    global O
    os.system("cls")
    print("============== Restaurante Brasileiro ==============\n")
    print("[1] Gerenciar Funcionários")
    print("[2] Gerenciar Pratos")
    print("[3] Gerenciamento Financeiro")
    print("[4] Lista Cardápio")
    print("[5] Realizar Venda")
    print("[6] Sair \n")

    O = input("Digite Uma Número: ")
    while O != 6:
        if O.isdigit():
            X = int(float(O))
            if X == 1:
                employee_management()
            elif X == 2:
                dish_management()
            elif X == 3:
                financial_management()
            elif X == 4:
                os.system("cls")
                print("============== Cardápio Da Casa ==============\n")
                print("=-==-==-==-==-==-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                list_dish()
                input("\nAperte 'ENTER' Para Voltar")
                Main_Menu()
            elif X == 5:
                sales_management()
            elif X != 6:
                input("\nOpção Não Existe\n")
                Main_Menu()
            elif X == 6:
                # keyboard.press_and_release("ctrl+c")
                print("\nOBRIGADO POR USAR O SISTEMA🥳\n")
                pyautogui.hotkey("ctrl+c")
                break
            else:
                input("\nAperte 'ENTER' Para Continuar\n")
        else:
            input("\nVocê Digitou Uma Letra | Tente Um Número Válido\n")
            Main_Menu()
        break


# Gerenciamento De Funcionários
def employee_management():
    os.system("cls")
    O = 0
    print("============== Gerenciar Funcionários ==============\n")
    print("[1] Cadastrar")
    print("[2] Editar")
    print("[3] Excluir")
    print("[4] Listar")
    print("[5] Voltar\n")

    O = input("Digite Uma Opção Desejada: ")

    while O != 6:
        if O.isdigit():
            X = int(float(O))
            if X == 1:
                os.system("cls")
                print("============== Informe Os Dados ==============\n")
                list = ObjEmployee.getShow()
                Name = input("Nome: ")
                Occupation = input("Função: ")
                new_employee = Employee(Name, Occupation)
                ObjEmployee.Add(new_employee)
                print("")
                print("Funcionario Cadastrado Com Sucesso Voltando Para Menu Principal")
            elif X == 2:
                os.system("cls")
                print("=-==-==-==-==-==-==-=-=-=-=-=-=-=\n")
                list = ObjEmployee.getShow()
                list_employees()
                print("\n=-==-==-==-==-==-==-=-=-=-=-=-=-=\n")

                print("")
                Edit_Id = int(input("Qual Cod?: "))
                res_name = int(input("Editar Nome? 1-[SIM] 2-[Não]: "))

                if res_name == 1:
                    Edit_Name = input("Novo Nome: ")
                    list[Edit_Id - 1].SetNome(Edit_Name)
                elif res_name == 2:
                    print("\nNome Não Alterado\n")

                res_ccupation = int(input("Editar Função? 1-[SIM] 2-[Não]: "))

                if res_ccupation == 1:
                    Edit_Occupation = input("Nova Função: ")
                    list[Edit_Id - 1].SetOccupation(Edit_Occupation)
                    print("\nFunção Atualizada")
                elif res_ccupation == 2:
                    print("\nNome Atualizado Com Sucesso Voltando Para Menu Principal")
            elif X == 3:
                os.system("cls")
                print("=-==-==-==-==-==-==-=-=-=-=-=-=-=\n")
                list = ObjEmployee.getShow()
                list_employees()
                print("\n=-==-==-==-==-==-==-=-=-=-=-=-=-=\n")
                Del_Id = int(input("Qual Código Deseja Excluir: "))

                print(f"Deseja Excluir: {list[Del_Id - 1].getNome()}?\n")
                res = int(input("Tem Certeza? 1-[SIM] 2-[Não]: "))
                print("")
                if res == 1:
                    ObjEmployee.Delete(list[Del_Id - 1])
                    print(
                        "Funcionario Excluido Com Sucesso Voltando Para Menu Principal"
                    )
                elif res == 2:
                    print("OK! Voltando Para Menu Principal")
            elif X == 4:
                os.system("cls")
                print("============== Lista De Funcionários ==============\n")
                list_employees()
            elif X == 5:
                os.system("cls")
                Main_Menu()
                break
            elif X != 5:
                print("\nOpção Não Existe")
        else:
            input("\nVocê Digitou Uma Letra | Tente Um Número Válido\n")
            employee_management()
        input("\nAperte 'ENTER' Para Continuar\n")
        employee_management()
        break


# Gerenciamento De Pratos
def dish_management():
    os.system("cls")
    O = 0
    print("============== Gerenciar Pratos ==============\n")
    print("[1] Cadastrar")
    print("[2] Editar")
    print("[3] Excluir")
    print("[4] Listar")
    print("[5] Voltar\n")

    O = input("Digite Uma Opção Desejada: ")

    while O != 6:
        if O.isdigit():
            X = int(float(O))
            if X == 1:
                os.system("cls")
                print("=-==-=-=-=-=-=-= Informe Os Dados =-==-=-=-=-=-=-= \n")
                Name = str(input("Nome: "))
                Description = str(input("Descrição: "))
                Price = int(input("Preço: "))
                print("")
                new_dish = Dish(Name, Description, Price)
                ObjDish.Add(new_dish)
                print("Prato Cadastrado Com Sucesso Voltando Para Menu Principal")
            elif X == 2:
                os.system("cls")
                print("=-==-==-==-==-==-==-=-=-=-=-=-=-=\n")
                list = ObjDish.getShow()
                list_dish()
                print("\n=-==-==-==-==-==-==-=-=-=-=-=-=-=\n")
                print("")
                Edit_Id = int(input("Qual Cod?: "))

                res_name = int(input("Editar Nome? 1-[SIM] 2-[Não]: "))
                if res_name == 1:
                    Edit_Nome = input("\nNovo Nome: ")
                    list[Edit_Id - 1].SetNome(Edit_Nome)
                elif res_name == 2:
                    print("\nNome Não Mudou")
                print("")

                res_description = int(input("Mudar Descrição? 1-[SIM] 2-[Não]: "))
                if res_description == 1:
                    Edit_Description = input("\nNova Descrição: ")
                    list[Edit_Id - 1].SetDescription(Edit_Description)
                elif res_description == 2:
                    print("\nDescrição Não Mudou")
                print("")

                res_price = int(input("Mudar Preço? 1-[SIM] 2-[Não]: "))
                if res_price == 1:
                    Edit_Price = int(input("\nNovo Preço: "))
                    list[Edit_Id - 1].SetPrice(Edit_Price)
                elif res_price == 2:
                    print("\nPreço Não Mudou")

            elif X == 3:
                os.system("cls")
                print("=-==-==-==-==-==-==-=-=-=-=-=-=-=\n")
                list = ObjDish.getShow()
                list_dish()
                print("\n=-==-==-==-==-==-==-=-=-=-=-=-=-=\n")

                Del_Id = int(input("Qual Cod Deseja Excluir?: "))
                print(f"Tem Certeza Que Vai Excluir: {list[Del_Id - 1].getNome()}\n")
                res = int(input("Tem Certeza? 1-[SIM] 2-[Não]: "))
                print("")

                if res == 1:
                    ObjDish.Delete(list[Del_Id - 1])
                    print("Prato Excluido Com Seucesso Voltando Para Menu Principal")
                elif res == 2:
                    print("OK! Voltando Para Menu Principal")
            elif X == 4:
                os.system("cls")
                print("============== Lista De Pratos ==============\n")
                list_dish()
            elif X == 5:
                os.system("cls")
                Main_Menu()
                break
            elif X != 5:
                print("\nOpção Não Existe")
        else:
            input("\nVocê Digitou Uma Letra | Tente Um Número Válido\n")
            dish_management()
        input("\nAperte 'ENTER' Para Continuar\n")
        dish_management()
        break


# Realizar Venda
def sales_management():
    os.system("cls")
    print("=-==-==-==-==-==-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
    list_Dish = ObjDish.getShow()
    list_Sales = ObjSales.getShow()
    list_dish()
    print("\n=-==-==-==-==-==-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
    Sale_Id = int(input("Cod. Do Prato Desejável?: "))
    print("")
    print(
        f"Você Vai Querer: {list_Dish[Sale_Id - 1].getNome()} | Custo: R$ {list_Dish[Sale_Id - 1].getPrice()}\n"
    )
    res = input("Tem Certeza: 1-[Sim] 2-[Não]: ")
    if res.isdigit():
        X = int(float(res))
        if X == 1:
            Amount_Paid = int(input("\nDigite O Valor A Ser Pago: R$ "))

            if Amount_Paid < list_Dish[Sale_Id - 1].getPrice():
                input("Valor Insuficiente Amigo!")
            elif Amount_Paid >= list_Dish[Sale_Id - 1].getPrice():
                print(
                    f"Você Tem Um Troco De: R$ {Amount_Paid - list_Dish[Sale_Id - 1].getPrice()}"
                )
                print("")
                new_sale = Sales(
                    list_Dish[Sale_Id - 1].getNome(), list_Dish[Sale_Id - 1].getPrice()
                )
                ObjSales.Add(new_sale)
                input("Venda Realizado Com Sucesso! Voltando Para Menu")
                Main_Menu()
        if X == 2:
            input("Venda Cancelado!")
            Main_Menu()
    else:
        input("\nVocê Digitou Uma Letra | Tente Um Número Válido\n")
        sales_management()


# Gerenciamento Financeiro
def financial_management():
    os.system("cls")
    O = 0
    print("============== Gerenciamento Financeiro ==============\n")
    print("[1] Listar Todas As Vendas")
    print("[2] Mostrar Lucro Total")
    print("[3] Voltar\n")

    O = input("Digite Uma Opção Desejada: ")

    while O != 4:
        if O.isdigit():
            X = int(float(O))
            if X == 1:
                os.system("cls")
                print("============== Totas As Vendas ==============\n")
                list_sales()
                input("\nAperte 'Enter' Para Voltar\n")
                financial_management()
            elif X == 2:
                print("SEM LUCRO")
                input("\nAperte 'Enter' Para Voltar\n")
                financial_management()
            elif X == 3:
                Main_Menu()
            elif X != 4:
                input("\nOpção Não Existe\n")
                financial_management()
        else:
            input("\nVocê Digitou Uma Letra | Tente Um Número Válido\n")
            financial_management()


# lista Funcionários
def list_employees():
    # Lista Funcionários
    list = ObjEmployee.getShow()
    if (len(list)) == 0:
        print("Nenhum Funcionário Cadastrado")
    else:
        for x in range(0, len(list)):
            print(f"Cod: {x + 1} | {list[x]}")


# Lista Pratos
def list_dish():
    # Lista De Pratos
    list = ObjDish.getShow()
    for x in range(0, len(list)):
        print(f"Cod: {x + 1} | {list[x]}")


# Lista Vendas
def list_sales():
    list = ObjSales.getShow()
    if (len(list)) == 0:
        print("Nenhuma Venda Realizada")
    else:
        for x in range(0, len(list)):
            print(f"Cod: {x + 1} | {list[x]}")


Main_Menu()

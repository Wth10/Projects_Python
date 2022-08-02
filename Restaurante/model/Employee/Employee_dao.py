from model.Employee.Employee import Employee

list_employee = []


def Add(x: Employee):
    list_employee.append(x)


def Delete(x: Employee):
    list_employee.remove(x)


def getShow() -> list:
    return list_employee

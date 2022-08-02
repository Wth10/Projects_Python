from model.Sales.Sales import Sales

list_sales = []


def Add(x: Sales):
    list_sales.append(x)


def Delete(x: Sales):
    list_sales.remove(x)


def getShow() -> list:
    return list_sales

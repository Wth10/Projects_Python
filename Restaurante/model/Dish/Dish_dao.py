from model.Dish import Dish

list_Dish = []


def Add(x: Dish):
    list_Dish.append(x)


def Delete(x: Dish):
    list_Dish.remove(x)


def getShow() -> list:
    return list_Dish

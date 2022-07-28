import httpx
from Classe import Bank

url_base = "https://brasilapi.com.br/api/"


def getBanks():
    list_banks = []
    url = f"{url_base}banks/v1"
    res = Connection(url)

    for x in res:
        new_bank = Bank(x["ispb"], x["name"], x["code"], x["fullName"])
        list_banks.append(new_bank)
    return list_banks


def getCEP(CEP):
    url = f"{url_base}cep/v1/{CEP}"
    res = Connection(url)
    return res


def getCNPJ(CNPJ):
    url = f"{url_base}cnpj/v1/{CNPJ}"
    res = Connection(url)
    return res


def getDDD(DDD):
    url = f"{url_base}ddd/v1/{DDD}"
    res = Connection(url)
    return res


def getHolidays(Holidays):
    url = f"{url_base}feriados/v1/{Holidays}"
    res = Connection(url)
    return res


def Connection(url):
    req = httpx.get(url)
    res = req.json()
    return res

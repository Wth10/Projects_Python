import httpx

url_base = "https://covid19-brazil-api.vercel.app/api/report/v1"


def getAll():
    return connectionApi(url_base)


def getUf(uf: str):
    url = f"{url_base}/brazil/uf/{uf}"
    data = connectionApi(url)
    return data


def connectionApi(url):
    request = httpx.get(url)
    response = request.json()
    return response


def getDate(date: str):
    url_date = f"{url_base}/brazil/{date}"
    data = connectionApi(url_date)
    return data

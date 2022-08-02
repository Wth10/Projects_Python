class Bank:
    def __init__(self, ispb, name, code, fullName) -> None:
        self.ispb = ispb
        self.name = name
        self.code = code
        self.fullName = fullName

    def print(self):
        print(f"Nome: {self.name} | Cod: {self.code}")


class CEp:
    def __init__(self, cep, state, city, service) -> None:
        self.cep = cep
        self.state = state
        self.city = city
        self.service = service


class CNPj:
    pass


class DDd:
    def __init__(self, state, cities) -> None:
        self.state = state
        self.cities = cities

    def print(self):
        print(f"Estado: {self.state} | Cidade: {self.cities}")

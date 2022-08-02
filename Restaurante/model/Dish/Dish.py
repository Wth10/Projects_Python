class Dish:
    def __init__(self, Nome, Description, Price) -> None:
        self.Nome = Nome
        self.Description = Description
        self.Price = Price

    def __str__(self):
        return (
            f"Nome: {self.Nome} | Descrição: {self.Description} | Preço: {self.Price}"
        )

    def getNome(self):
        return self.Nome

    def getPrice(self):
        return self.Price

    def SetNome(self, New_Nome):
        self.Nome = New_Nome

    def SetDescription(self, New_Description):
        self.Description = New_Description

    def SetPrice(self, New_Price):
        self.Price = New_Price

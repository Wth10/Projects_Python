class Sales:
    def __init__(self, Nome_Prato, Price_Prato) -> None:
        self.Nome_Prato = Nome_Prato
        self.Price_Prato = Price_Prato

    def __str__(self):
        return f"Nome: {self.Nome_Prato} | Valor Do Prato: {self.Price_Prato}"

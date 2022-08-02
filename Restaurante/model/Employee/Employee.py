class Employee:
    def __init__(self, Nome, Occupation) -> None:
        self.Nome = Nome
        self.Occupation = Occupation

    def __str__(self):
        return f"Nome: {self.Nome} | Função: {self.Occupation}"

    def getNome(self):
        return self.Nome

    def SetNome(self, New_Nome):
        self.Nome = New_Nome

    def SetOccupation(self, New_Occupation):
        self.Occupation = New_Occupation

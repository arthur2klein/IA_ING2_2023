class Objet:
    def __init__(self, masse: int, valeur: int):
        self.masse = masse;
        self.valeur = valeur;

    def densite(self) -> float:
        return self.valeur / self.masse;

    def __str__(self) -> str:
        return "Objet de masse {} et de valeur {}"\
            .format(self.masse, self.valeur);
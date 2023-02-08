from cmath import sqrt


class Statistiques:
    def __init__(self):
        self.lValeurs: list[float] = [];

    def ajouter(self, valeur: float):
        self.lValeurs += [valeur];
        self.lValeurs.sort();

    def min(self) -> float:
        return self.lValeurs[0];

    def max(self) -> float:
        return self.lValeurs[-1];

    def percentile(self, position: float) -> float:
        indice = position * len(self.lValeurs);
        indiceEntier = int(indice);
        indiceDecimal = indice - indiceEntier;
        return self.lValeurs[indiceEntier] * (1 - indiceDecimal) + \
               self.lValeurs[indiceEntier + 1] * indiceDecimal;

    def mediane(self) -> float:
        return self.percentile(0.5);

    def moyenne(self) -> float:
        res = 0.;
        for valeur in self.lValeurs:
            res += valeur;
        return res / len(self.lValeurs);

    def variance(self) -> float:
        res = 0.;
        for valeur in self.lValeurs:
            res += valeur * valeur;
        moyenne = self.moyenne;
        return res / len(self.lValeurs) - moyenne() * moyenne();

    def ecartType(self) -> float:
        return sqrt(self.variance());
        
    def __str__(self) -> str:
        return "Statistiques : \n \
               min = {}\n\
               \tmax = {}\n\
               \tmoyenne = {}\n\
               \tmediane = {}\n\
               \tecart type = {}"\
               .format(self.min(),
                       self.max(),
                       self.moyenne(),
                       self.mediane(),
                       self.ecartType()
                    );
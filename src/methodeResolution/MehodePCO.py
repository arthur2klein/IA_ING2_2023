from methodeResolution.Methode import Methode
from probleme.Probleme import Probleme
from solution.Essaim import Essaim


class MethodePCO(Methode):
    def __init__(self, probleme: Probleme, nEtapes: int):
        self.probleme = probleme;
        self.nEtapes = nEtapes;

    def resoudre(self) -> Essaim:
        res = self.probleme.candidat();
        for i in range(self.nEtapes):
            res = self.probleme.voisin(res);
        return res;
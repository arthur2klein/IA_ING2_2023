from methodeResolution.Methode import Methode
from probleme.ProblemeEssaim import ProblemeEssaim
from solution.Essaim import Essaim


class MethodePCO(Methode):
    def __init__(self, probleme: ProblemeEssaim, nEtapes: int):
        self.probleme = probleme;
        self.nEtapes = nEtapes;

    def resoudre(self) -> Essaim:
        optimum = self.probleme.candidat();
        res = self.probleme.candidat();
        for i in range(self.nEtapes):
            res = self.probleme.voisin(res);
            if (res.evaluer() < optimum.evaluer()):
                optimum = Essaim.fromEssaim(res);
        return optimum;
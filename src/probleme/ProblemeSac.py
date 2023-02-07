import random
from outils.Objet import Objet
from probleme.Probleme import Probleme
from solution.Sac import Sac

class ProblemeSac(Probleme):
    def __init__(self, lObjets: list[Objet], capacite: int):
        self.lObjets = lObjets;
        self.capacite = capacite;
    
    def candidat(self) -> Sac:
        return Sac.fromCapacite(self.capacite);

    def voisin(self, candidat: Sac) -> Sac:
        indice = random.randrange(len(self.lObjets));
        res = Sac.fromSac(candidat);
        res.ajouter(self.lObjets[indice]);
        res.fixer();
        return res;

    def getObjets(self) -> list[Objet]:
        return self.lObjets[:];
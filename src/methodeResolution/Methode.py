from outils.Statistiques import Statistiques
from solution.Solution import Solution


class Methode:
    def resoudre(self) -> Solution:
        raise NotImplementedError;

    def tester(self, nIterations: int) -> Statistiques:
        res = Statistiques();
        for i in range(nIterations):
            res.ajouter(self.resoudre().evaluer());
        return res;
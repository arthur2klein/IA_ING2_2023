import random
from outils.Point import Point
from probleme.Probleme import Probleme
from solution.Chemin import Chemin


class ProblemeTSP(Probleme):
    def __init__(self, lPoints):
        self.lPoints: list[Point] = lPoints;
    
    def candidat(self) -> Chemin:
        points = self.lPoints[:];
        random.shuffle(points);
        return Chemin(points);

    def voisin(self, candidat: Chemin) -> Chemin:
        indice1 = random.randrange(len(self.lPoints));
        indice2 = random.randrange(len(self.lPoints));
        res = Chemin.fromChemin(candidat);
        res.inverserEntre(indice1, indice2);
        return res;
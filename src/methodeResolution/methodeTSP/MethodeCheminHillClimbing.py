import math
import random
from methodeResolution.Methode import Methode
from outils.Point import Point
from probleme.ProblemeTSP import ProblemeTSP
from solution.Chemin import Chemin


class MethodeCheminHillClimbing(Methode):
    def __init__(self, probleme: ProblemeTSP):
        self.probleme = probleme;
        self.lPoints = probleme.lPoints;

    def resoudre(self) -> Chemin:
        res = candidat(self.lPoints);
        for i in range (int(math.sqrt(len(self.lPoints)))):
            newCandidat = candidat(self.lPoints);
            if (newCandidat.evaluer() < res.evaluer()):
                res = newCandidat;
        return res;

def candidat(lPoints: list[Point]) -> Chemin:
    res = Chemin([]);
    restants = lPoints.copy();
    indice = random.randint(0, len(restants) - 1);
    pointChoisi = restants[indice];
    res.addPoint(pointChoisi);
    restants.pop(indice);
    while restants:
        closest = restants[0];
        for p in restants:
            if (
                p.distance(res.getDernier()) <
                closest.distance(res.getDernier())
            ):
                closest = p;
        res.addPoint(closest);
        restants.remove(closest);
    return res;

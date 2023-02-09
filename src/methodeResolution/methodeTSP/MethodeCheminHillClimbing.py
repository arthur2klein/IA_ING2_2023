import math
import random
from methodeResolution.Methode import Methode
from outils.Point import Point
from probleme.ProblemeTSP import ProblemeTSP
from solution.Chemin import Chemin


class MethodeCheminHillClimbing(Methode):
    """Method to solve the TSP by using the Hill Climbing method.
    An initial point is randomly chosen and the nearest point is added to the
    path until all points have been visited once.
    """
    def __init__(self, probleme: ProblemeTSP):
        """Create a method of resolution of the given TSP using the Hill
        Climbing Method.

        Args:
            probleme (ProblemeTSP): _description_
        """
        self.probleme = probleme;
        self.lPoints = probleme.lPoints;

    def resoudre(self) -> Chemin:
        """Solve the TSP of the instance using the Hill Climbing method.
        An initial point is randomly chosen and the nearest point is added to
        the path until all points have been visited once.

        Returns:
            Chemin: Best of √(#(lpoints)) path found using the Hill Climbing
            method.
        """
        res = candidat(self.lPoints);
        for i in range (int(math.sqrt(len(self.lPoints)))):
            newCandidat = candidat(self.lPoints);
            if (newCandidat.evaluer() < res.evaluer()):
                res = newCandidat;
        return res;

def candidat(lPoints: list[Point]) -> Chemin:
    """Create one path going through each of the given points once by following
    the Hill Climbing method from a random point.

    Args:
        lPoints (list[Point]): List of points that should be visited once by
        the path.

    Returns:
        Chemin: Path found through the given points by following the Hill
        Climbing method from a random point.
    """
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

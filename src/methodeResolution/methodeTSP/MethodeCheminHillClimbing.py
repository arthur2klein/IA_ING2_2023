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
        return min(
            (
                self.candidat()
                for _ in range(int(math.sqrt(len(self.lPoints))))
            ),
            key = lambda x: x.evaluer()
        );

    def candidat(self) -> Chemin:
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
        restants = self.lPoints[:];
        indice = random.randint(a = 0, b = len(restants) - 1);
        pointChoisi = restants[indice];
        res.addPoint(point = pointChoisi);
        restants.pop(indice);
        while restants:
            closest = min(
                restants,
                key = lambda x: x.distance(other = res.getDernier())
            );
            res.addPoint(point = closest);
            restants.remove(closest);
        return res;

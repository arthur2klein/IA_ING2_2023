import random
from outils.Point import Point
from probleme.Probleme import Probleme
from solution.Chemin import Chemin


class ProblemeTSP(Probleme):
    """TSP
    """
    def __init__(self, lPoints: list[Point]):
        """Create a TSP with the given list of points to visit.

        Args:
            lPoints (list[Point]): Points that will have to be visited.
        """
        self.lPoints: list[Point] = lPoints;
    
    def candidat(self) -> Chemin:
        """Create a random path through all the cities.

        Returns:
            Chemin: Random path passing through all the cities exactly once.
        """
        points = self.lPoints[:];
        random.shuffle(points);
        return Chemin(chemin = points);

    def voisin(self, candidat: Chemin) -> Chemin:
        """Create a neighbour of the given path by reversing a randomly chosen
        portion of the path.

        Args:
            candidat (Chemin): Path to search a neighbour of.

        Returns:
            Chemin: Neighbour of the given path.
        """
        indice1 = random.randrange(len(self.lPoints));
        indice2 = random.randrange(len(self.lPoints));
        res = Chemin.fromChemin(chemin = candidat);
        res.inverserEntre(indice1 = indice1, indice2 = indice2);
        return res;
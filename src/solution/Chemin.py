from __future__ import annotations
from outils.Point import Point
from solution.Solution import Solution


class Chemin(Solution):
    """A path solving the TSP.
    """
    def __init__(self, chemin: list[Point]):
        """Create a path.

        Args:
            chemin (list[Point]): List of points in the order that they will be
            travearsed.
        """
        self.points: list[Point] = chemin[:];

    def fromChemin(chemin: Chemin) -> Chemin:
        """Copy the given path.

        Args:
            chemin (Chemin): Path to copy.

        Returns:
            Chemin: Copy of the path.
        """
        res = Chemin(chemin = chemin.points[:]);
        return res;

    def addPoint(self, point: Point):
        """Add a point to the path.

        Args:
            point (Point): Point to add at the end of the path.
        """
        self.points += [point];
        
    def getDernier(self) -> Point:
        """Get the last visited point.

        Returns:
            Point: Last point of the path.
        """
        return self.points[-1];

    def inverserEntre(
        self,
        indice1: int,
        indice2: int
    ):
        """Reverse the slice of the path between the two given indices.

        Args:
            indice1 (int): First index.
            indice2 (int): Second index.
        """
        for i in range(indice1, int((indice1 + indice2) / 2)):
            self.inverser(indice1 = indice1, indice2 = indice2);

    def inverser(
        self,
        indice1: int,
        indice2: int
    ):
        """Reverse the two points of given indices in the path.

        Args:
            indice1 (int): First index.
            indice2 (int): Second index.
        """
        temp = self.points[indice1];
        self.points[indice1] = self.points[indice2];
        self.points[indice2] = temp;

    def __str__(self) -> str:
        """Create a string with all the information about the path.

        Returns:
            str: String containing all the information about the path.
        """
        res = "";
        for i in range (len(self.points)):
            res += self.points[i].nom + ";";
        return res;
        
    def evaluer(self) -> float:
        """Determine the total length of the path.

        Returns:
            float: Total length of the path.
        """
        res = 0.;
        for i in range(1, len(self.points)):
            res += self.points[i - 1].distance(other = self.points[i]);
        return res + self.points[0].distance(other = self.points[-1]);
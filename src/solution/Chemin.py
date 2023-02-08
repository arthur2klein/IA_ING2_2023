from outils.Point import Point
from solution.Solution import Solution


class Chemin(Solution):
    def __init__(self, chemin: list[Point]):
        self.points: list[Point] = chemin[:];

    def fromChemin(chemin):
        res = Chemin(chemin.points[:]);
        return res;

    def addPoint(self, point: Point):
        self.points += [point];
        
    def getDernier(self) -> Point:
        return self.points[-1];

    def inverserEntre(self, indice1: int, indice2: int):
        for i in range(indice1, int((indice1 + indice2) / 2)):
            self.inverser(indice1, indice2);

    def inverser(self, indice1: int, indice2: int):
        temp = self.points[indice1];
        self.points[indice1] = self.points[indice2];
        self.points[indice2] = temp;

    def __str__(self) -> str:
        res = "";
        for i in range (len(self.points)):
            res += self.points[i].nom + ";";
        return res;
        
    def evaluer(self) -> float:
        res = 0.;
        for i in range(1, len(self.points)):
            res += self.points[i - 1].distance(self.points[i]);
        return res + self.points[0].distance(self.points[-1]);
from solution.Solution import Solution;

class Probleme:
    def candidat(self) -> Solution:
        raise NotImplementedError;
    def voisin(self, candidat: Solution) -> Solution:
        raise NotImplementedError;
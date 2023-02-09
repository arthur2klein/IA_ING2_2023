import random
from methodeResolution.Methode import Methode
from probleme.ProblemeTSP import ProblemeTSP
from solution.Chemin import Chemin


class MethodeCheminAleatoire(Methode):
    """Method to find a random solution to the TSP.
    """
    def __init__(self, problemeTSP: ProblemeTSP):
        """Create a method to search a random solution to the given TSP.

        Args:
            problemeTSP (ProblemeTSP): TSP to solve.
        """
        self.probleme = problemeTSP;
        self.lPoints = problemeTSP.lPoints;
        
    def resoudre(self) -> Chemin:
        """Find a random solution of the TSP corresponding to the instance.

        Returns:
            Chemin: Best of the 1000⋅#(lpoints) path randomly created.
        """
        nbIter = 1000 * len(self.lPoints);
        optimum = self.genererChemin();
        distanceOptimale = optimum.evaluer();
        for i in range(nbIter - 1):
            nouveauChemin = self.genererChemin();
            nouvelleLongueur = nouveauChemin.evaluer();
            if (nouvelleLongueur < distanceOptimale):
                distanceOptimale = nouvelleLongueur;
                optimum = nouveauChemin;
        return optimum;

    def genererChemin(self) -> Chemin:
        """Create a random path going through each of the points only once.

        Returns:
            Chemin: Path randomly created.
        """
        res = self.lPoints[:];
        random.shuffle(res);
        return Chemin(res);
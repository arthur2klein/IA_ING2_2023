from methodeResolution.Methode import Methode
from probleme.ProblemeTSP import ProblemeTSP
from solution.Chemin import Chemin;
from outils.Point import Point;

import random;

class mehodeCheminAleatoire(Methode):
    def __init__(self, problemeTSP: ProblemeTSP):
        self.probleme = problemeTSP;
        self.lPoints = problemeTSP.lPoints;
        
    def resoudre(self) -> Chemin:
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
        res = self.lPoints[:];
        random.shuffle(res);
        return Chemin(res);
import math
import random
from methodeResolution.Methode import Methode
from probleme.Probleme import Probleme
from solution.Solution import Solution


class MethodeRecuit(Methode):
    def __init__(
        self,
        probleme: Probleme,
        refroidissement: float,
        tempInitiale: float,
        tempMin: float,
        iterationsParTemp: int
    ):
        self.probleme = probleme;
        self.refroidissement = refroidissement;
        self.tempInitiale = tempInitiale
        self.tempMin = tempMin;
        self.iterationsParTemp = iterationsParTemp;

    def resoudre(self) -> Solution:
        solution = self.probleme.candidat();
        evaluation = solution.evaluer();
        optimum = solution;
        minEval = evaluation;
        temperature = self.tempInitiale;
        while (temperature > self.tempMin):
            for i in range(self.iterationsParTemp):
                voisin = self.probleme.voisin(solution);
                delta = voisin.evaluer() - evaluation;
                if (critereMetropolis(delta, temperature)):
                    solution = voisin;
                    evaluation = solution.evaluer();
                    if (delta < 0 and evaluation < minEval):
                        minEval = evaluation;
                        optimum = voisin;
            temperature *= self.refroidissement;
        return optimum;

def critereMetropolis(delta: float, temperature: float) -> bool:
    if (delta <= 0):
        return True;
    return random.random() < math.exp(-delta / temperature);
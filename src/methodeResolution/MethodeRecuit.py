import math
import random
from methodeResolution.Methode import Methode
from probleme.Probleme import Probleme
from solution.Solution import Solution


class MethodeRecuit(Methode):
    """Method to solve a problem with the Simulated Annealing method.
    This method is simular to the Hill Climbing method but worse candidates
    could be randomly chosen based on how much worse they are, and how much
    comparaison has already been done.
    """
    def __init__(
        self,
        probleme: Probleme,
        refroidissement: float,
        tempInitiale: float,
        tempMin: float,
        iterationsParTemp: int
    ):
        """Create a method of resolution of the given problem using the
        Simulated Annealing method with the given parameters.

        Args:
            probleme (Probleme): Problem to solve.
            refroidissement (float): Multiplication factor of the temperature
            for each plateau.
            tempInitiale (float): Initial temperature.
            tempMin (float): Temperature at which the resolution is finished.
            iterationsParTemp (int): Number of iterations to do before reducing
            the temperature.
        """
        self.probleme = probleme;
        self.refroidissement = refroidissement;
        self.tempInitiale = tempInitiale;
        self.tempMin = tempMin;
        self.iterationsParTemp = iterationsParTemp;

    def resoudre(self) -> Solution:
        """Solve the problem of the instance using the Simulated Annealing
        method.
        This method is simular to the Hill Climbing method but worse candidates
        could be randomly chosen based on how much worse they are, and how much
        comparaison has already been done.

        Returns:
            Solution: Best solution found by the Simulated Annealing method.
        """
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
    """Indicate if a point should be chosen because it is better than the
    precedent point, or randomly if the point is not too much worse
    (The chances of chosing a worse point are exp(-𝜟/T)).

    Args:
        delta (float): Difference of evaluation between the current evaluation
        and the former best evaluation.
        temperature (float): Temperature of the system.

    Returns:
        bool: True iff the evaluation of the new point is better or is not
        worse enough for the new point not to be randomly chosen.
    """
    return delta <= 0 or\
           random.random() < math.exp(-delta / temperature);
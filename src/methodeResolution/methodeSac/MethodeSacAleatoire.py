import random
from methodeResolution.methodeSac.MethodeSacTri import MethodeSacTri
from outils.Objet import Objet
from probleme.ProblemeSac import ProblemeSac


class MethodeSacAleatoire(MethodeSacTri):
    """Mehode to create a random solution to the knapsack problem.
    """
    def __init__(self, probleme: ProblemeSac):
        """Create a method of random resolution of the given knapsack problem.

        Args:
            probleme (ProblemeSac): Knapsack problem to solve
        """
        self.probleme = probleme;
    
    def trier(self, objets: list[Objet]):
        """Randomly shuffle a given list of Objet.

        Args:
            objets (list[Objet]): List of Objet to shuffle.
        """
        random.shuffle(objets);
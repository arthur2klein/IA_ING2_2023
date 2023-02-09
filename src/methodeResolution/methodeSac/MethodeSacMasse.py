from methodeResolution.methodeSac.MethodeSacTri import MethodeSacTri
from outils.Objet import Objet
from probleme.Probleme import Probleme


class MethodeSacMasse(MethodeSacTri):
    """Mehod of resolution of the knapsack problem prioritazing the lightest
    objects.
    """
    def __init__(self, probleme: Probleme):
        """Create a method of resolution of the given knapsack problem that
        will prioritaze the lightest objects.

        Args:
            probleme (Probleme): Knapsack problem to solve.
        """
        self.probleme = probleme;
    
    def trier(self, objets: list[Objet]):
        """Sort the given list of objects based on their increasing weight.

        Args:
            objets (list[Objet]): List of objects to sort.
        """
        objets.sort(key = lambda objet : objet.masse);
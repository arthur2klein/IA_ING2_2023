from methodeResolution.methodeSac.MethodeSacTri import MethodeSacTri
from outils.Objet import Objet
from probleme.Probleme import Probleme


class MethodeSacDensite(MethodeSacTri):
    """Mehod to solve the knapsack problem by prioritazing the objects with the
    best density of value.
    """
    def __init__(self, probleme: Probleme):
        """Create a method of resolution of the given knapsack problem that
        will based its decisions on the density of value of the objects.

        Args:
            probleme (Probleme): Knapsack problem to solve.
        """
        self.probleme = probleme;
    
    def trier(self, objets: list[Objet]):
        """Sort the given list of object by density of value.

        Args:
            objets (list[Objet]): List of object to sort.
        """
        objets.sort(key = lambda objet : -objet.densite());
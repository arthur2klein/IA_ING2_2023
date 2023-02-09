from methodeResolution.methodeSac.MethodeSacTri import MethodeSacTri
from outils.Objet import Objet
from probleme.Probleme import Probleme


class MethodeSacValeur(MethodeSacTri):
    """Method solving the knapsack problem by prioritazing the objects with
    the highest value.
    """
    def __init__(self, probleme: Probleme):
        """Create a method of resolution of the given knapsack problem that
        will place the highest value objects first.

        Args:
            probleme (Probleme): Knapsack problem to sort.
        """
        self.probleme = probleme;
    
    def trier(self, objets: list[Objet]):
        """Sort the given list of objects by decreasing value.

        Args:
            objets (list[Objet]): List of objects to sort.
        """
        objets.sort(key = lambda objet : -objet.valeur);
import random
from outils.Objet import Objet
from probleme.Probleme import Probleme
from solution.Sac import Sac


class ProblemeSac(Probleme):
    """Knapsack problem.
    """
    def __init__(
        self,
        lObjets: list[Objet],
        capacite: int
    ):
        """Create a knapsack problem with the given objects and capacity.

        Args:
            lObjets (list[Objet]): List of objects to place in the bag.
            capacite (int): Maximal capacity of the bag.
        """
        self.lObjets = lObjets;
        self.capacite = capacite;
    
    def candidat(self) -> Sac:
        """Create an empty bag with the capacity of the problem.

        Returns:
            Sac: Empy bag with the correct capacity.
        """
        return Sac.fromCapacite(self.capacite);

    def voisin(self, candidat: Sac) -> Sac:
        """Create a neighbour of the given bag.
        Add or remove one object and remove randomly chosen objects if the bag
        is too heavy.

        Args:
            candidat (Sac): Bag to search a neighbour for.

        Returns:
            Sac: Neighbour of the given bag.
        """
        indice = random.randrange(len(self.lObjets));
        res = Sac.fromSac(candidat);
        res.ajouter(self.lObjets[indice]);
        res.fixer();
        return res;

    def getObjets(self) -> list[Objet]:
        return self.lObjets[:];
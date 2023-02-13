from __future__ import annotations
import random
from outils.Objet import Objet
from solution.Solution import Solution


class Sac(Solution):
    """Bag for the knapsack problem.
    """
    def __init__(
            self,
            capacite: int,
            contenu: list[Objet]
        ):
        """Create a bag with the given content and capacity.

        Args:
            capacite (int): Maximal capacity of the bag.
            contenu (list[Objet]): Content of the bag.
        """
        self.capacite: int = capacite;
        self.contenu: list[Objet] = contenu;
    
    def fromCapacite(capacite: int) -> Sac:
        """Create an empty bag with the given capacity.

        Args:
            capacite (int): Capacity of the bag.

        Returns:
            Sac: Empty bag with the given capacity.
        """
        return Sac(capacite = capacite, contenu = []);

    def fromSac(sac: Sac) -> Sac:
        """Copy a given bag.

        Args:
            sac (Sac): Bag to copy.

        Returns:
            Sac: Copy of the given bag.
        """
        return Sac(capacite = sac.capacite, contenu = sac.contenu[:]);

    def evaluer(self) -> float:
        """Determine the total value of the content of the bag.

        Returns:
            float: Sum of the values of the items in the bag.
        """
        res = 0.;
        for objet in self.contenu:
            res += objet.valeur;
        return res;

    def ajouter(self, objet: Objet):
        """Add an item to the bag.

        Args:
            objet (Objet): Item to add to the current bag.
        """
        self.contenu += [objet];
    
    def retirer(self, objet: Objet):
        """Remove an item from the bag.

        Args:
            objet (Objet): Item to remove from the bag.
        """
        self.contenu.remove(objet);

    def contient(self, objet: Objet) -> bool:
        """Determine wheter the current bag contains a given object.

        Args:
            objet (Objet): Object to search in the bag.

        Returns:
            bool: True iff the bag contains the given object.
        """
        return objet in self.contenu;

    def toggle(self, objet: Objet):
        """Add the given object to the bag or removes it if it is already in
        the bag.

        Args:
            objet (Objet): Object to add to or remove from the bag.
        """
        if (self.contient(objet = objet)):
            self.retirer(objet = objet);
        else:
            self.ajouter(objet = objet)

    def masseContenu(self) -> int:
        """Total weight of the bag.

        Returns:
            int: Sum of the weights of the items contained in the bag.
        """
        res = 0;
        for objet in self.contenu:
            res += objet.masse;
        return res;

    def estTropPlein(self) -> bool:
        """Determine wether the bag is overweighted.

        Returns:
            bool: True iff the total weight of the content of the bag exceeds
            its capacity.
        """
        return self.masseContenu() > self.capacite;

    def fixer(self):
        """Removes randomly chosen objects from the bag until it is not
        overweighted anymore.
        """
        while(self.estTropPlein()):
            indice = random.randrange(len(self.contenu));
            objet = self.contenu[indice]
            self.retirer(objet = objet);

    def __str__(self) -> str:
        """Create a string with all the information about the bag.

        Returns:
            str: String containing all the information about the bag.
        """
        res = "Sac:";
        for objet in self.contenu:
            res += "\n\t{}".format(objet);
        return res;
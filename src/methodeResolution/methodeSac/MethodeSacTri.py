from methodeResolution.Methode import Methode
from outils.Objet import Objet
from solution.Sac import Sac


class MethodeSacTri(Methode):
    """Interface for methods of resolution of the knapsack problem which will sort
    a list of elements to prioritaze which of them should be added.
    """
    def resoudre(self) -> Sac:
        """Solve the knapsack problem with the current method.

        Returns:
            Sac: Best Sac found using this method.
        """
        objets = self.probleme.getObjets();
        self.trier(objets)
        sac = self.probleme.candidat();
        for objet in objets:
            sac.ajouter(objet = objet);
            if (sac.estTropPlein()):
                sac.retirer(objet = objet);
        return sac;
    
    def trier(self, objets: list[Objet]):
        """Function implemented by the children to sort the given list of
        objects by priority.

        Args:
            objets (list[Objet]): List of objects to sort.

        Raises:
            NotImplementedError: This is an abstract method and it is only
            implemented by the children classes.
        """
        raise NotImplementedError;
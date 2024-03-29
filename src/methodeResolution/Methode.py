from outils.Statistiques import Statistiques
from solution.Solution import Solution


class Methode:
    """Interface for methods of resolution of problems.
    """
    def resoudre(self) -> Solution:
        """Solve the problem of the instance.

        Raises:
            NotImplementedError: This is an abstract function and it is only
            implemented by the children classes.

        Returns:
            Solution: Solution of the problem found by the instance.
        """
        raise NotImplementedError;

    def tester(self, nIterations: int) -> Statistiques:
        """Test the current method by solving a given number of times the same
        problem.

        Args:
            nIterations (int): Number of times that the problem should be
            solved.

        Raises:
            ValueError: nIterations should be positive.

        Returns:
            Statistiques: Statistics of all the results of the resolutions.
        """
        if (nIterations <= 0):
            raise ValueError("Number of iterations are positive.");
        res = Statistiques();
        for progression in range(nIterations):
            print (f'{progression / nIterations * 100.:05.2f}%', end="\r");
            res.ajouter(valeur = self.resoudre().evaluer());
        return res;
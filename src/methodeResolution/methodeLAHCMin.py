from methodeResolution.Methode import Methode
from probleme.Probleme import Probleme
from solution.Solution import Solution


class MethodeLAHCMin(Methode):
    """Method to solve a problem using the LAHC method to minimize the
    evaluation.
    The LAHC method is similar to an Hill Climbing method but new values are
    compared to older values rather that from the last one.
    """
    def __init__(
            self,
            probleme: Probleme,
            tailleMem: int,
            nIter: int
        ):
        """Create a method to solve a given problem using the LAHC method with
        a given memory size and number of iteration.

        Args:
            probleme (Probleme): Problem to solve.
            tailleMem (int): Size of the memory to use to store older
            encountered points.
            nIter (int): Number of iterations of Hill Climbing.
        """
        self.probleme = probleme;
        self.tailleMem = tailleMem;
        self.nIter = nIter;

    def resoudre(self) -> Solution:
        """Solve the problem of the instance using the LAHC method to minimize
        the evaluation.

        Returns:
            Solution: Candidate found with the lowest evaluation.
        """
        candidat = self.probleme.candidat();
        valeurCandidat = candidat.evaluer();
        optimum = candidat;
        valeurMin = valeurCandidat;
        tabMemoire = [valeurMin for _ in range(self.tailleMem)];
        for n in range(1, self.nIter):
            voisin = self.probleme.voisin(candidat = candidat);
            valMem = tabMemoire[n % self.tailleMem];
            if (valMem >= voisin.evaluer()):
                candidat = voisin;
            tabMemoire[n % self.tailleMem] = candidat.evaluer();
            if (valeurMin > voisin.evaluer()):
                optimum = voisin;
                valeurMin = voisin.evaluer();
        return optimum;

            
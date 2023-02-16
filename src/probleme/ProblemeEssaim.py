from typing import Callable
from outils.Particule import Particule
from probleme.Probleme import Probleme
from solution.Essaim import Essaim


class ProblemeEssaim(Probleme):
    """Continuous problem to solve using the PSO.
    In the PSO, a swarm of particules are randomly placed in a space assigning a
    value to each point and the particules try to find the best points by
    following: their own inertia; the best position they have individually
    found; the best position their group has found.
    """
    def __init__(
        self,
        fonction: Callable[[list[float]], float],
        nDimensions: int,
        borneInf: float,
        borneSup: float,
        estDansMemeGroupe: Callable[[Particule, Particule], bool],
        tailleEssaim: int,
        inertie: float,
        maxConfiance: float
    ):
        """Create a continuous problem that can be solved using the PSO.

        Args:
            fonction (Callable[[list[float]): Function to search the minimum of.
            nDimensions (int): Number of dimensions of the search space.
            borneInf (float): Lower bound of the search space.
            borneSup (float): Upper bound of the search space.
            estDansMemeGroupe (Callable[[Particule, Particule], bool]): Function
            determining wether of not two given particules are in the same
            group.
            tailleEssaim (int): Size of the swarm to use for the optimisation.
            inertie (float): Inertia of the particules of the swarm.
            maxConfiance (float): Maximal confidence of the particules of the
            swarm regarding the best position found by themselves and their
            groups.
        """
        self.fonction = fonction;
        self.tailleEssaim = tailleEssaim;
        self.borneInf = borneInf;
        self.borneSup = borneSup;
        self.estDansMemeGroupe = estDansMemeGroupe;
        self.nDimensions = nDimensions;
        self.inertie = inertie;
        self.maxConfiance = maxConfiance;

    def candidat(self) -> Essaim:
        """Create the swarm that will solve the problem.
        The particules are placed randomly in the search space and have no
        initail speed.

        Returns:
            Essaim: Swarm that will solve the problem.
        """
        return Essaim.createSwarm(
            self.fonction,
            self.estDansMemeGroupe,
            self.borneInf,
            self.borneSup,
            self.nDimensions,
            self.tailleEssaim,
            self.inertie,
            self.maxConfiance
        );

    def voisin(self, candidat: Essaim) -> Essaim:
        """Let the swarm do a step of speed update and movement.

        Args:
            candidat (Essaim): Swarm to let do a step.

        Returns:
            Essaim: Same swarm as in parameter.
        """
        if (candidat == None):
            return self.candidat();
        candidat.etape();
        return candidat;
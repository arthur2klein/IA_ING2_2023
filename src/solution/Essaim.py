from __future__ import annotations
import random
from typing import Callable
from outils.Particule import Particule
from solution.Solution import Solution


class Essaim(Solution):
    """Swarm for the PSO.
    """
    def __init__(
        self,
        fonction: Callable[[list[float]], float],
        estDansMemeGroupe: Callable[[Particule, Particule], bool],
        particules: list[Particule]
    ):
        """Create a swarm of particules from a list of particules.

        Args:
            fonction (Callable[[list[float]], float]): Function that the swarm
            will try to minimize.
            estDansMemeGroupe (Callable[[Particule, Particule], bool]): _description_
            Function that determine wheter of not two particules are in a same
            group.
            particules (list[Particule]): Particules of the swarm.
        """
        self.fonction = fonction;
        self.estDansMemeGroupe = estDansMemeGroupe;
        self.particules = particules;
        
    def createSwarm(
        fonction: Callable[[list[float]], float],
        estDansMemeGroupe: Callable[[Particule, Particule], bool],
        borneInf: float,
        borneSup: float,
        nDimensions: int,
        taille: int,
        inertie: float,
        maxConfiance: float,
    ) -> Essaim:
        """Create a swarm of particules from scratch.

        Args:
            fonction (Callable[[list[float]], float]): Function that the swarm
            will try to minimize.
            estDansMemeGroupe (Callable[[Particule, Particule], bool]):
            Function that determine wheter of not two particules are in a same
            group.
            borneInf (float): Lower bound of the search space.
            borneSup (float): Upper bound of the serach space.
            nDimensions (int): Number of dimensions of the search space.
            taille (int): Number of particules in the swarm.
            inertie (float): Inertia of the particules of the swarm.
            maxConfiance (float): Maximal confidence of the particules of the
            swarm regarding the best position that they and their group has
            already found.
        
        Returns:
            Essaim: New swarm with the parameters.
        """
        return Essaim(
            fonction,
            estDansMemeGroupe,
            [Particule(
                    i,
                    inertie,
                    maxConfiance,
                    [random.random() * (borneSup - borneInf) + borneInf
                    for i in range(nDimensions)],
                    borneInf,
                    borneSup
                ) for i in range(taille)]
        );

    def fromEssaim(essaim: Essaim) -> Essaim:
        """Copy the given swarm.

        Args:
            essaim (Essaim): Swarm to copy.

        Returns:
            Essaim: Copy of the given swarm.
        """
        return Essaim(
            essaim.fonction,
            essaim.estDansMemeGroupe,
            [Particule.fromParticule(x) for x in essaim.particules]
        );
    
    def meilleurPos(self) -> list[float]:
        """Determine the best position occupated by the swarm.

        Returns:
            list[float]: Best position occupated by the swarm.
        """
        res = None;
        for particule in self.particules:
            if (
                res == None or
                self.valeur(particule) < self.valeur(particule)
            ):
                res = particule;
        return res.position;
        
    def evaluer(self) -> float:
        """Determine the evaluation of the best position occupated by the
        swarm.

        Returns:
            float: Evaluation of the best position occupated by the swarm.
        """
        res = None;
        for particule in self.particules:
            valeur = self.valeur(particule);
            if (res == None or valeur < res):
                res = valeur;
        return res;

    def valeurPos(self, position: list[float]) -> float:
        """Determine the evaluation of a given position.

        Args:
            position (list[float]): Position to evaluate.

        Returns:
            float: Evaluation of the given position.
        """
        return self.fonction(position);

    def valeur(self, particule: Particule) -> float:
        """Determine the evaluation of the position of a given particule.

        Args:
            particule (Particule): Particule whose position will be evaluated.

        Returns:
            float: Evaluation of the position of the given particule.
        """
        return self.valeurPos(particule.position);

    def etape(self):
        """Do a step of speed update and movement.
        """
        for particule in self.particules:
            particule.majVitesse(self.meilleurGroupe(particule));
        for particule in self.particules:
            particule.seDeplacer();
            if (
                self.valeur(particule) <
                self.valeurPos(particule.preferee)
            ):
                particule.majPreferee();

    def meilleurGroupe(self, particule: Particule) -> list[float]:
        """Determine the position of the particule of the group of a given
        particule that has the best evaluation.

        Args:
            particule (Particule): Particule from which the best particule of
            the group will be determined.

        Returns:
            list[float]: Best position of the group.
        """
        res = particule.preferee;
        for autre in self.particules:
            if (not self.estDansMemeGroupe(particule, autre)):
                continue;
            if (
                self.valeurPos(autre.preferee) <
                self.valeurPos(res)
            ):
                res = autre.preferee[:];
        return res;

    def __str__(self) -> str:
        """Print most of the information about the particules of the current
        swarm.

        Returns:
            str: String containing most of the information about the particule
            of the current swarm.
        """
        res = "Essaim:";
        for particule in self.particules:
            res += "\n\t{} : evaluation = {:0.2E}"\
                .format(
                    particule.__str__(),
                    self.valeur(particule)
                );
        return res;
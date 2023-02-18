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
            estDansMemeGroupe (Callable[[Particule, Particule], bool]):
            Function that determine wheter of not two particules are in a same
            group.
            particules (list[Particule]): Particules of the swarm.
        """
        self.fonction = fonction;
        self.estDansMemeGroupe = estDansMemeGroupe;
        self.particules = particules;
        for particule in self.particules:
            particule.valeur = self.fonction(particule.position);
            particule.valeurPreferee = particule.valeur;
        
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
            fonction = fonction,
            estDansMemeGroupe = estDansMemeGroupe,
            particules = [Particule(
                id = i,
                inertie = inertie,
                maxConfiance = maxConfiance,
                position = [
                    random.random() * (borneSup - borneInf) + borneInf
                    for _ in range(nDimensions)
                ],
                borneInf = borneInf,
                borneSup = borneSup
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
            fonction = essaim.fonction,
            estDansMemeGroupe = essaim.estDansMemeGroupe,
            particules = [Particule.fromParticule(particule = x)
                          for x in essaim.particules]
        );

    def etape(self):
        """Do a step of speed update and movement.
        """
        for particule in self.particules:
            particule.majVitesse(cible = self.meilleurGroupe(particule));
        for particule in self.particules:
            particule.seDeplacer();
            particule.valeur = self.fonction(particule.position);
            if (
                self.valeur(particule = particule) <
                particule.valeurPreferee
            ):
                particule.majPreferee();
                particule.valeurPreferee = particule.valeur;
    
    def meilleurParticule(self) -> Particule:
        """Determine the best particule of the swarm.

        Returns:
            Particule: Best particule of the swarm.
        """
        return min(
            (
                particule
                for particule in self.particules
            ),
            key = lambda x: self.valeur(x)
        );

    def meilleurGroupe(self, particule: Particule) -> list[float]:
        """Determine the position of the particule of the group of a given
        particule that has the best evaluation.

        Args:
            particule (Particule): Particule from which the best particule of
            the group will be determined.

        Returns:
            list[float]: Best position of the group.
        """
        return min(
            (
                p for p in self.particules
                if self.estDansMemeGroupe(particule, p)
            ),
            key = lambda x: x.valeurPreferee 
        ).preferee;
        
    def meilleurPos(self) -> list[float]:
        """Determine the best position occupated by the swarm.

        Returns:
            list[float]: Best position occupated by the swarm.
        """
        return self.meilleurParticule().position;

    def valeur(self, particule: Particule) -> float:
        """Determine the evaluation of the position of a given particule.

        Args:
            particule (Particule): Particule whose position will be evaluated.

        Returns:
            float: Evaluation of the position of the given particule.
        """
        return particule.valeur;
        
    def evaluer(self) -> float:
        """Determine the evaluation of the best position occupated by the
        swarm.

        Returns:
            float: Evaluation of the best position occupated by the swarm.
        """
        return min(
            self.valeur(particule)
            for particule in self.particules
        );

    def __str__(self) -> str:
        """Print most of the information about the particules of the current
        swarm.

        Returns:
            str: String containing most of the information about the particule
            of the current swarm.
        """
        return (
            f'Essaim:'
            f'\nMeilleure particule: {self.meilleurParticule()}'
            f'\nEvaluation: {self.evaluer():> 12,.5E}'
        );
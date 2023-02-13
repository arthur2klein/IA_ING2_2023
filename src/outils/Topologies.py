from typing import Callable
from outils.Particule import Particule


class Topologie:
    """Contains all the functions which could be used to determine wheter or
    not two particules are in a same group.
    """
    def tousMemeGroupe(particule1: Particule, particule2: Particule) -> bool:
        """Assume that all particules are in the same group.

        Args:
            particule1 (Particule): First particule.
            particule2 (Particule): Second particule.

        Returns:
            bool: Always true as all particules are in a same group.
        """
        return True;

    def _cycle(
        nParticules: int,
        particule1: Particule,
        particule2: Particule
    ) -> bool:
        """Assume that the topology is a cycle.

        Args:
            nParticules (int): Total number of particules.
            particule1 (Particule): First particule.
            particule2 (Particule): Second particule.

        Returns:
            bool: True iff the particules follow each other in the cycle.
        """
        return (particule1.id + 1) % nParticules == particule2.id or\
               (particule2.id + 1) % nParticules == particule1.id;

    def cycle(
        nParticules: int
    ) -> Callable[[Particule, Particule], bool]:
        """Create a fonction which assumes that the particules topology is a
        cycle.

        Args:
            nParticules (int): Total number of particules.

        Returns:
            Callable[[Particule, Particule], bool]: Function returning true
            iff the two given particules follow each orther in a cycle.
        """
        return lambda p1, p2: Topologie._cycle(
            nParticules = nParticules,
            particule1 = p1,
            particule2 = p2
        );

    def roue(particule1: Particule, particule2: Particule) -> bool:
        """Assume that all particules are only neighbour to the first one.

        Args:
            particule1 (Particule): First particule.
            particule2 (Particule): Second particule.

        Returns:
            bool: True iff one of the particule is the one with the 0 id as it
            is the only neighbour of all other particules.
        """
        return particule1.id == 0 or particule2.id == 0 or\
               particule1.id == particule2.id;

    def _clustersDeTaille(
        taille: int,
        particule1: Particule,
        particule2: Particule
    ) -> bool:
        """Assume that there are a given number of particules per groups.

        Args:
            taille (int): Number of particules per cluster.
            particule1 (Particule): First particule.
            particule2 (Particule): Second particule.

        Returns:
            bool: True iff the particules are in a same group of the given size.
        """
        id1modn = particule1.id % taille;
        id1overn = particule1.id // taille;
        id2modn = particule2.id % taille;
        id2overn = particule2.id // taille;
        return id1overn == id2overn or\
            (id1modn == id2overn and id1overn == id2modn);

    def clustersDeTaille(taille: int) -> Callable[[Particule, Particule], bool]:
        """Create a function assuming that they are n particules per group.

        Args:
            taille (int): Number of particules per group.

        Returns:
            Callable[[Particule, Particule], bool]: Function that will allow to
            ensure that two given particules are in a same group of the given
            size.
        """
        return lambda p1, p2: Topologie._clustersDeTaille(
            taille = taille,
            particule1 = p1,
            particule2 = p2
        );

    def _vonNeumann(
        largeur: int,
        longueur: int,
        particule1: Particule,
        particule2: Particule
    ) -> bool:
        """Assumes that the particules are in a von Neumann topology.

        Args:
            largeur (int): Width of the grid.
            longueur (int): Length of the grid.
            particule1 (Particule): First particule.
            particule2 (Particule): Second particule.

        Returns:
            bool: True iff the two particules are in a same von Neumann
            topology.
        """
        taille = largeur * longueur;
        id1 = particule1.id;
        id2 = particule2.id;
        return (id1 + 1) % largeur == id2 or\
               (id2 + 1) % largeur == id1 or\
               (id1 + largeur) % taille == id2 or\
               (id2 + largeur) % taille == id1 or\
               id1 == id2;

    def vonNeumann(
        largeur: int,
        longueur: int
    ) -> Callable[[Particule, Particule], bool]:
        """Create a function which will assume that the particules are bound in
        a von Neumann topology.
        Each particule has four neighbours like if they where arranged in a
        two-dimensional grid wrapped in the border.

        Args:
            largeur (int): Width of the grid.
            longueur (int): Length of the grid.

        Returns:
            Callable[[Particule, Particule], bool]: Function that will allow to
            ensure that two given particules are neighbour in a von Neumann
            topology.
        """
        return lambda p1, p2: Topologie._vonNeumann(
            largeur = largeur,
            longueur = longueur,
            particule1 = p1,
            particule2 = p2
        );
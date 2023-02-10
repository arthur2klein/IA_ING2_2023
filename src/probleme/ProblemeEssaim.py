import math
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
        candidat.etape();
        return candidat;

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

    def tousDifferents(particule1: Particule, particule2: Particule) -> bool:
        """Assume that all particules are in different groups.

        Args:
            particule1 (Particule): First particule.
            particule2 (Particule): Second particule.

        Returns:
            bool: Always false as all particule are in different groups.
        """
        return False;

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

    def _nMemeGroupe(
        n: int,
        particule1: Particule,
        particule2: Particule
    ) -> bool:
        """Assume that there are a given number of particules per groups.

        Args:
            n (int): Number of particules per group.
            particule1 (Particule): First particule.
            particule2 (Particule): Second particule.

        Returns:
            bool: True iff the particules are in a same group of the given size.
        """
        return particule1.id // n == particule2.id // n;

    def _nGroupes(
        n: int,
        particule1: Particule,
        particule2: Particule
    ) -> bool:
        """Assume that there are a given number of groups.

        Args:
            n (int): Number of groups.
            particule1 (Particule): First particule.
            particule2 (Particule): Second particule.

        Returns:
            bool: True iff the particules are in the same group between the
            given number of groups.
        """
        return particule1.id % n == particule2.id % n;

    def nombreParGroupe(n: int) -> Callable[[Particule, Particule], bool]:
        """Create a function assuming that they are n particules per group.

        Args:
            n (int): Number of particules per group.

        Returns:
            Callable[[Particule, Particule], bool]: Function that will allow to
            ensure that two given particules are in a same group of the given
            size.
        """
        return lambda p1, p2: Topologie._nMemeGroupe(n, p1, p2);

    def nombreGroupe(n: int) -> Callable[[Particule, Particule], bool]:
        """Create a function which will assume that they are n groups.

        Args:
            n (int): Number of groups.

        Returns:
            Callable[[Particule, Particule], bool]: Function that will allow to
            ensure that two given particules are in a same group between the
            given number of groups.
        """
        return lambda p1, p2: Topologie._nGroupes(n, p1, p2);

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
               (id2 + largeur) % taille == id1;

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
        return lambda p1, p2: Topologie._vonNeumann(largeur, longueur, p1, p2);

# Probleme Sphere
def sphere(position: list[float]) -> float:
    """Sphere function
    f(x1, ..., xn) = ∑(xi²)

    Args:
        position (list[float]): Antecedent.

    Returns:
        float: Image of the given antecedent by the sphere function.
    """
    res: float = 0.;
    for x in position:
        res += x * x;
    return res;

sphere.borneInf = -5.12;
sphere.borneSup = 5.12;

# Probleme Schwefel
def schwefel(position: list[float]) -> float:
    """Schwefel function
    f(x1, ..., xn) = 418.9829⋅n - ∑(xi - sin(√(|xi|)))

    Args:
        position (list[float]): Antecedent.

    Returns:
        float: Image of the given antecedent by the schwefel function.
    """
    res: float = 0.;
    for x in position:
        res += x * math.sin(math.sqrt(math.fabs(x)));
    return 418.9829 * len(position) - res;

schwefel.borneInf = -500;
schwefel.borneSup = 500;

# Probleme Rosenbrock
def rosenbrock(position: list[float]) -> float:
    """Rosenbrock function
    f(x1, ..., xn) = ∑(100 ⋅ (x{i+1} - xi²)² + (xi - 1)²)

    Args:
        position (list[float]): Antecedent.

    Returns:
        float: Image of the given antecedent by the rosenbrock function.
    """
    res: float = 0.;
    for i in range(len(position) - 1):
        xi = position[i];
        xip1 = position[i + 1];
        m1 = (xip1 - xi * xi);
        m2 = xi - 1;
        res += 100 * m1 * m1 + m2 * m2;
    return res;

rosenbrock.borneInf = -2.048;
rosenbrock.borneSup = 2.048;

# Probleme Griewank
def griewank(position: list[float]) -> float:
    """Griewank function
    f(x1, ..., xn) = ∏(cos(xi/√(i+1))) + ∑(xi²/4000)

    Args:
        position (list[float]): _description_

    Returns:
        float: _description_
    """
    res: float = 1.;
    for i in range(len(position)):
        res *= math.cos(position[i] / math.sqrt(i + 1));
    for x in position:
        res += x * x / 4000.;
    return res + 1.;

griewank.borneInf = -600;
griewank.borneSup = 600;
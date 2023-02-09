from __future__ import annotations
import math
import random


class Particule:
    """A particule of the PSO method.
    """
    def __init__(
        self,
        id: int,
        inertie: float,
        maxConfiance: float,
        position: list[float],
        borneInf: float,
        borneSup: float
    ):
        """Create a new particule with the given caracteristics.

        Args:
            id (int): Id of the particule.
            inertie (float): Inertia that the particule will have when updating
            its speed.
            maxConfiance (float): How much maximal confidence the particule
            will have regarding the best position she and its group found when
            updating its speed.
            position (list[float]): Position of the particule.
            borneInf (float): Lower bound of the space that the particule
            should explorate.
            borneSup (float): Upper bound of the space that the particule
            should explorate.
        """
        self.id = id;
        self.inertie = inertie;
        self.maxConfiance = maxConfiance;
        self.position = position;
        self.preferee = position[:];
        self.vitesse = [0. for i in self.position];
        self.borneInf = borneInf;
        self.borneSup = borneSup;
        self.limVitesse = (borneSup - borneInf) * 0.5;

    def fromParticule(particule: Particule) -> Particule:
        """Create a new particule from a given one.

        Args:
            particule (Particule): Particule to copy.

        Returns:
            _type_: Copy of the given particule.
        """
        return Particule(
            particule.id,
            particule.inertie,
            particule.maxConfiance,
            particule.position[:],
            particule.borneInf,
            particule.borneSup
        );

    def majVitesse(self, cible: list[float]):
        """Update the speed of the particule.
        The update forumla is:
        v(k+1)=v(k)⋅inertia + (x(k)-xCible)⋅r1⋅maxConf + (x(k)-xBest)⋅r2⋅maxConf
        where:
        - inertia is the inertia of the particule,
        - maxConf is the maximal possible confidence tha the particule could
        have to the best value she found and the target that the swarm give it,
        - r1 is a random value between 0 and 1,
        - r2 is a random value between 0 and 1,
        - v(k) is the speed of the kth step,
        - v(k+1) is the new speed,
        - x(k) is the current position of the particule,
        - xBest is the best position that the particule has found,
        - xCible is the position of a partciule that the swarm wants the
        particule to follow.

        Args:
            cible (list[float]): Position the the swarm wants the particule to
            reach.
        """
        confiancePreferee = random.random() * self.maxConfiance;
        confianceCible = random.random() * self.maxConfiance;
        self.vitesse = [
            self.inertie * self.vitesse[i] +
            confianceCible * (cible[i] - self.position[i]) +
            confiancePreferee * (self.preferee[i] - self.position[i])
            for i in range(len(self.vitesse))
        ];

    def seDeplacer(self):
        """Move according to its speed.
        """
        # self.limiterVitesse();
        # self.limiterAuxBornes();
        self.position = [self.position[i] + self.vitesse[i]
                         for i in range(len(self.position))];
        self.replacerPositionDansEspacePeriodique();
        # self.replacerPositionDansEspaceRebond();
    
    def replacerPositionDansEspaceRebond(self):
        """Keep the particule in the search space by making it bounce from the
        boundaries.
        """
        largeurEspace = self.borneSup - self.borneInf;
        for i in range(len(self.position)):
            composante = self.position[i];
            while (
                composante < self.borneInf or
                composante > self.borneSup
            ):
                if composante > self.borneSup:
                    composante = 2 * self.borneSup - composante;
                if composante < self.borneInf:
                    composante = 2 * self.borneInf - composante;
            self.position[i] = composante;

    def limiterVitesse(self):
        """Limit the speed of the particule to try to keep it in the reasearch
        space.
        """
        n = norme(self.vitesse);
        if (n > self.limVitesse):
            coef = self.limVitesse / n;
            self.vitesse = [v * coef for v in self.vitesse];
        
    def replacerPositionDansEspacePeriodique(self):
        """Keep the particule in the search space by re-placing it assuming the
        space is periodic.
        """
        largeurEspace = self.borneSup - self.borneInf;
        for i in range(len(self.position)):
            composante = self.position[i];
            while composante > self.borneSup:
                composante -= largeurEspace;
            while composante < self.borneInf:
                composante += largeurEspace;
            self.position[i] = composante;
        
    def limiterAuxBornes(self):
        """Keep the particule in the search space by ensuring that, if the
        current speed should bring it outside of the space, it stops when
        reaching the boundaries of the space instead.
        """
        for i in range(len(self.vitesse)):
            ###################################################################
            # On est en position p avec une vitesse v
            # Si p + v > sup, on veut p + v' = sup
            # Donc v' = sup - p
            # On multiplie donc le vecteur vitesse par sup - p / v
            # 
            # On est en position pi avec une vitesse v
            # Si p + v < inf, on veut p + v' = inf
            # Donc v' = inf - p
            # On multiplie donc le vecteur vitesse par inf - p / v
            # 
            # #################################################################
            positionPrevue = self.vitesse[i] + self.position[i];
            if positionPrevue > self.borneSup:
                ratio = (self.borneSup - self.position[i]) / self.vitesse[i];
                self.vitesse = [
                    composante * ratio
                    for composante in self.vitesse
                ];
            if positionPrevue < self.borneInf:
                ratio = (self.borneInf - self.position[i]) / self.vitesse[i];
                self.vitesse = [
                    composante * ratio
                    for composante in self.vitesse
                ];

    def majPreferee(self):
        """Update the best position known by the particule to match the current
        position of the particule.
        """
        self.preferee = self.position[:];

    def estDansBorne(self) -> bool:
        """Verify if the particule is in the boundaries of the search zone.

        Returns:
            bool: True iff the particule is in the boundaries of the search
            zone.
        """
        for x in self.position:
            if x > self.borneSup:
                return False;
            if x < self.borneInf:
                return False;
        return True;

    def __str__(self) -> str:
        """Create a string containing the informations of the current
        particule.

        Returns:
            str: String containing the informations (id, position and norm of
            the speed) of the current particule.
        """
        return "Particule d'id {} en position {} avec une vitesse {:0.2E}"\
            .format(
                self.id,
                ["{0:0.2E}".format(pos) for pos in self.position],
                norme(self.vitesse)
            );


def norme(liste: list[float]) -> float:
    """Calculate the norm of the given values.

    Args:
        liste (list[float]): Values to calculate the norm of.

    Returns:
        float: Norm of the values of the given list.
    """
    res = 0.;
    for x in liste:
        res += x * x;
    return math.sqrt(res);

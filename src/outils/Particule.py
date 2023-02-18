from __future__ import annotations
from enum import auto
import math
import random

class EnumBH:
    """Enumeration of method of Boundary handling:
    - ARRET_FRONTIERE stops the particule when reaching the boundary,
    - REBOND_FRONTIERE makes the particule bounde when reaching the boundary,
    - PLUS_PROCHE_FRONTIERE bring the particule back to the nearest point of
    the space.
    - LIMITE_VITESSE limits the speed of the particule to ensure that it does
    not go to far from the boundary,
    - ESPACE_PERIODIQUE places the particule back in the boundary like if the
    space was periodic.
    """
    ARRET_FRONTIERE = auto();    
    REBOND_FRONTIERE = auto();    
    PLUS_PROCHE_FRONTIERE = auto();    
    LIMITE_VITESSE = auto();    
    ESPACE_PERIODIQUE = auto();    

class Particule:
    """A particule of the PSO method.
    """
    bhMethod: EnumBH = EnumBH.REBOND_FRONTIERE;

    def __init__(
        self,
        id: int,
        inertie: float,
        maxConfiance: float,
        position: list[float],
        borneInf: float,
        borneSup: float,
        fonction: callable[[list[float]], float]
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
            fonction (callable[[list[float]], float]): Fonction to optimize.
        """
        self.id = id;
        self.inertie = inertie;
        self.maxConfiance = maxConfiance;
        self.position = position;
        self.preferee = position[:];
        self.vitesse = [0.] * len(self.position);
        self.borneInf = borneInf;
        self.borneSup = borneSup;
        self.fonction = fonction;
        self.valeur = fonction(self.position);
        self.valeurPreferee = self.valeur;
        self.groupe = [];
        self.limVitesse = (borneSup - borneInf) * 0.5;
        match (Particule.bhMethod):
            case EnumBH.ARRET_FRONTIERE:
                self._seDeplacer = self._seDeplacerArretFrontiere;
            case EnumBH.REBOND_FRONTIERE:
                self._seDeplacer = self._seDeplacerRebondFrontiere;
            case EnumBH.PLUS_PROCHE_FRONTIERE:
                self._seDeplacer = self._seDeplacerPlusProcheFrontiere;
            case EnumBH.LIMITE_VITESSE:
                self._seDeplacer = self._seDeplacerLimiteVitesse;
            case EnumBH.ESPACE_PERIODIQUE:
                self._seDeplacer = self._seDeplacerEspacePeriodique;

    def fromParticule(particule: Particule) -> Particule:
        """Create a new particule from a given one.

        Args:
            particule (Particule): Particule to copy.

        Returns:
            Particule: Copy of the given particule.
        """
        return Particule(
            id = particule.id,
            inertie = particule.inertie,
            maxConfiance = particule.maxConfiance,
            position = particule.position[:],
            borneInf = particule.borneInf,
            borneSup = particule.borneSup,
            fonction = particule.fonction
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
            cible (list[float]): Position that the swarm wants the particule to
            reach.
        """
        confiancePreferee = random.random() * self.maxConfiance;
        confianceCible = random.random() * self.maxConfiance;
        self.vitesse = [
            self.inertie * vitessePrecedente +
            confianceCible * (direction - position) +
            confiancePreferee * (preferee - position)
            for position, vitessePrecedente, preferee, direction
            in zip(
                self.position,
                self.vitesse,
                self.preferee,
                cible
            )
        ];

    def seDeplacer(self):
        """Move according to its speed and boundary handling strategy.
        """
        self._seDeplacer();
        self.valeur = self.fonction(self.position);

    def _seDeplacerArretFrontiere(self):
        """Move according to its speed and considering that the particule
        stops when reaching a boundary.
        """
        def _coefToBoundary(pos: float, vit: float) -> float:
            """Returns the ratio of the given speed necessary for the
            particule not to go out of the boundary.

            Args:
                pos (float): Component of the position.
                vit (float): Component of the speed.

            Returns:
                float: Ratio nessary for particule not to go out of the
                boundary.
            """
            nextPos = pos + vit;
            if nextPos < self.borneInf:
                return (self.borneInf - pos) / vit;
            if nextPos > self.borneSup:
                return (self.borneSup - pos) / vit;
            return 1.;
        ratio = min(
            _coefToBoundary(pos, vit)
            for pos, vit in zip(self.position, self.vitesse)
        );
        if ratio < 1.:
            self.position = [
                pos + vit * ratio
                for pos, vit in zip(self.position, self.vitesse)
            ];
            self.vitesse = [0.] * len(self.position);
        else:
            self.position = [
                pos + vit
                for pos, vit in zip(self.position, self.vitesse)
            ];
    
    def _seDeplacerRebondFrontiere(self):
        """Move according to its speed and considering that the particule
        bounce when reaching a boundary.
        """
        self.position = [
            pos + vit
            for pos, vit in zip(self.position, self.vitesse)
        ];
        for i in range(len(self.position)):
            while (True):
                if self.position[i] > self.borneSup:
                    self.position[i] = 2 * self.borneSup - self.position[i];
                    self.vitesse[i] *= -1;
                elif self.position[i] < self.borneInf:
                    self.vitesse[i] *= -1;
                    self.position[i] = 2 * self.borneInf - self.position[i];
                else:
                    break;
    
    def _seDeplacerPlusProcheFrontiere(self):
        """Move according to its speed and considering that the particule
        glides along the boundaries.
        """
        self.position = [
            pos + vit
            for pos, vit in zip(self.position, self.vitesse)
        ];
        for i in range(len(self.position)):
            if self.position[i] > self.borneSup:
                self.position[i] = self.borneSup;
                self.vitesse[i] = 0;
            if self.position[i] < self.borneInf:
                self.position[i] = self.borneInf;
                self.vitesse[i] = 0;
        
    def _seDeplacerLimiteVitesse(self):
        """Move according to its speed and considering that the particule
        has a speed limit.
        """
        if ((n := norme(liste = self.vitesse)) > self.limVitesse):
            coef = self.limVitesse / n;
            self.vitesse = [v * coef for v in self.vitesse];
        self.position = [
            pos + vit
            for pos, vit in zip(self.position, self.vitesse)
        ];

    def _seDeplacerEspacePeriodique(self):
        """Move according to its speed and considering that the particule
        evolve in a periodic space.
        """
        largeurEspace = self.borneSup - self.borneInf;
        self.position = [
            (pos + vit - self.borneInf) % largeurEspace + self.borneInf
            for pos, vit in zip(self.position, self.vitesse)
        ];

    def majPreferee(self):
        """Update the best position known by the particule to match the current
        position of the particule.
        """
        self.preferee = self.position[:];
        self.valeurPreferee = self.valeur;

    def estDansBorne(self) -> bool:
        """Verify if the particule is in the boundaries of the search zone.

        Returns:
            bool: True iff the particule is in the boundaries of the search
            zone.
        """
        return all(self.borneInf < x < self.borneSup for x in self.position);

    def ajouterGroupe(self, particule: Particule):
        """Adds a particule to the group of the current particule.

        Args:
            particule (Particule): Particule to add to the group.
        """
        self.groupe += [particule];

    def __str__(self) -> str:
        """Create a string containing the informations of the current
        particule.

        Returns:
            str: String containing the informations (id, position and norm of
            the speed) of the current particule.
        """
        return f'Particule d\'id {self.id:3} avec position =' +\
               "".join(f'\n\t{pos:>+12.5E}' for pos in self.position);

def norme(liste: list[float]) -> float:
    """Calculate the norm of the given values.

    Args:
        liste (list[float]): Values to calculate the norm of.

    Returns:
        float: Norm of the values of the given list.
    """
    return math.sqrt(sum(x * x for x in liste));

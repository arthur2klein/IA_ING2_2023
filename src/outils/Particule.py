import math
import random


class Particule:
    def __init__(
        self,
        id: int,
        inertie: float,
        maxConfiance: float,
        position: list[float],
        borneInf: float,
        borneSup: float
    ):
        self.id = id;
        self.inertie = inertie;
        self.maxConfiance = maxConfiance;
        self.position = position;
        self.preferee = position[:];
        self.vitesse = [0. for i in self.position];
        self.borneInf = borneInf;
        self.borneSup = borneSup;
        self.limVitesse = (borneSup - borneInf) * 0.5;

    def fromParticule(particule):
        return Particule(
            particule.id,
            particule.inertie,
            particule.maxConfiance,
            particule.position[:],
            particule.borneInf,
            particule.borneSup
        );

    def majVitesse(self, cible: list[float]):
        confiancePreferee = random.random() * self.maxConfiance;
        confianceCible = random.random() * self.maxConfiance;
        self.vitesse = [
            self.inertie * self.vitesse[i] +
            confianceCible * (cible[i] - self.position[i]) +
            confiancePreferee * (self.preferee[i] - self.position[i])
            for i in range(len(self.vitesse))
        ];

    def seDeplacer(self):
        self.limiterVitesse();
        # self.limiterAuxBornes();
        self.position = [self.position[i] + self.vitesse[i]
                         for i in range(len(self.position))];
        self.replacerPositionDansEspacePeriodique();
        # self.replacerPositionDansEspaceRebond();
    
    def replacerPositionDansEspaceRebond(self):
        largeurEspace = self.borneSup - self.borneInf;
        for i in range(len(self.position)):
            composante = self.position[i];
            while composante < self.borneInf or composante > self.borneSup:
                if composante > self.borneSup:
                    composante = 2 * self.borneSup - composante;
                if composante < self.borneInf:
                    composante = 2 * self.borneInf - composante;
            self.position[i] = composante;

    def limiterVitesse(self):
        n = norme(self.vitesse);
        if (n > self.limVitesse):
            coef = self.limVitesse / n;
            self.vitesse = [v * coef for v in self.vitesse];
        
    def replacerPositionDansEspacePeriodique(self):
        largeurEspace = self.borneSup - self.borneInf;
        for i in range(len(self.position)):
            composante = self.position[i];
            while composante > self.borneSup:
                composante -= largeurEspace;
            while composante < self.borneInf:
                composante += largeurEspace;
            self.position[i] = composante;
        
    def limiterAuxBornes(self):
        for i in range(len(self.vitesse)):
            ##################"
            # On est en position pi avec une vitesse v1
            # Si p1 + v1 > sup, on veut p1 + v1' = sup
            # Donc v1' = sup - p1
            # On multiplie donc le vecteur vitesse par sup - p1 / v1
            # 
            # On est en position pi avec une vitesse v1
            # Si p1 + v1 < inf, on veut p1 + v1' = inf
            # Donc v1' = inf - p1
            # On multiplie donc le vecteur vitesse par inf - p1 / v1
            # 
            # #################"
            positionPrevue = self.vitesse[i] + self.position[i];
            if positionPrevue > self.borneSup:
                ratio = (self.borneSup - self.position[i]) / self.vitesse[i];
                self.vitesse = [composante * ratio for composante in self.vitesse];
            if positionPrevue < self.borneInf:
                ratio = (self.borneInf - self.position[i]) / self.vitesse[i];
                self.vitesse = [composante * ratio for composante in self.vitesse];

    def majPreferee(self):
        self.preferee = self.position[:];

    def estDansBorne(self) -> bool:
        for x in self.position:
            if x > self.borneSup:
                return False;
            if x < self.borneInf:
                return False;
        return True;

    def __str__(self):
        return "Particule d'id {} en position {} avec une vitesse {:0.2E}".format(self.id, ["{0:0.2E}".format(pos) for pos in self.position], norme(self.vitesse));


def norme(liste: list[float]) -> float:
    res = 0.;
    for x in liste:
        res += x * x;
    return math.sqrt(res);

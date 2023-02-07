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

    def majVitesse(self, cible):
        confiancePreferee = random.random() * self.maxConfiance;
        confianceCible = random.random() * self.maxConfiance;
        self.vitesse = [
            self.inertie * self.vitesse[i] +
            confianceCible * (cible.position[i] - self.position[i]) +
            confiancePreferee * (self.preferee[i] - self.position[i])
            for i in range(len(self.vitesse))
        ];
    
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

    def seDeplacer(self):
        self.position = [self.position[i] + self.vitesse[i]
                         for i in range(len(self.position))];
        self.replacerPositionDansEspacePeriodique();

    def majPreferee(self):
        self.preferee = self.position[:];

    def estDansBorne(self) -> bool:
        for x in self.position:
            if x > self.borneSup:
                return False;
            if x < self.borneInf:
                return False;
        return True;
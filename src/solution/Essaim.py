import random
from solution.Solution import Solution
from outils.Particule import Particule

class Essaim(Solution):
    def __init__(self, probleme, taille: int, inertie: float, maxConfiance: float):
        self.fonction = probleme.fonction;
        self.estDansMemeGroupe = probleme.estDansMemeGroupe;
        self.particules: list[Particule] = [
            Particule(
                i,
                inertie,
                maxConfiance,
                [random.random() * (probleme.borneSup - probleme.borneInf) + probleme.borneInf
                for i in range(probleme.nDimensions)],
                probleme.borneInf,
                probleme.borneSup
            )
            for i in range(taille)
        ];
    
    def meilleurPos(self) -> list[float]:
        res = None;
        for particule in self.particules:
            if (res == None or self.valeur(particule) < self.valeur(particule)):
                res = particule;
        return res.position;
        
    def evaluer(self) -> float:
        res = None;
        for particule in self.particules:
            valeur = self.valeur(particule);
            if (res == None or valeur < res):
                res = valeur;
        return res;

    def valeurPos(self, position: list[float]) -> float:
        return self.fonction(position);

    def valeur(self, particule: Particule) -> float:
        return self.valeurPos(particule.position);

    def etape(self):
        for particule in self.particules:
            particule.majVitesse(self.meilleurGroupe(particule));
        for particule in self.particules:
            particule.seDeplacer();
            if (self.valeur(particule) > self.valeurPos(particule.preferee)):
                particule.majPreferee;

    def meilleurGroupe(self, particule: Particule) -> Particule:
        res = None;
        for autre in self.particules:
            if (not self.estDansMemeGroupe(particule, autre)):
                continue;
            if (res == None or self.valeur(autre) < self.valeur((res))):
                res = autre;
        return res;

    def __str__(self) -> str:
        return "Essaim: meilleur position: {}".format(self.meilleurPos());
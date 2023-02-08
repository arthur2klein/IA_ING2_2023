import random
from outils.Particule import Particule
from solution.Solution import Solution


class Essaim(Solution):
    def __init__(
        self,
        fonction,
        estDansMemeGroupe,
        borneInf: float,
        borneSup: float,
        nDimensions: int,
        taille: int,
        inertie: float,
        maxConfiance: float,
    ):
        self.fonction = fonction;
        self.estDansMemeGroupe = estDansMemeGroupe;
        self.particules: list[Particule] = [
            Particule(
                i,
                inertie,
                maxConfiance,
                [random.random() * (borneSup - borneInf) + borneInf
                for i in range(nDimensions)],
                borneInf,
                borneSup
            )
            for i in range(taille)
        ];

    def fromEssaim(essaim):
        res = Essaim(
            essaim.fonction,
            essaim.estDansMemeGroupe,
            0,
            0,
            0,
            0,
            0,
            0
        );
        res.particules = [Particule.fromParticule(x) for x in essaim.particules];
        return res;
    
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
            if (self.valeur(particule) < self.valeurPos(particule.preferee)):
                particule.majPreferee();

    def meilleurGroupe(self, particule: Particule) -> list[float]:
        res = particule.preferee;
        for autre in self.particules:
            if (not self.estDansMemeGroupe(particule, autre)):
                continue;
            if (self.valeurPos(autre.preferee) < self.valeurPos(res)):
                res = autre.preferee[:];
        return res;

    def __str__(self) -> str:
        res = "Essaim:";
        for particule in self.particules:
            res += "\n\t{} : evaluation = {:0.2E}"\
                .format(
                    particule.__str__(),
                    self.valeur(particule)
                );
        return res;
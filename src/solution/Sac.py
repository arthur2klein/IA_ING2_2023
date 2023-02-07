import random
from solution.Solution import Solution
from outils.Objet import Objet

class Sac(Solution):
    def __init__(self, capacite: int, contenu: list[Objet]):
        self.capacite: int = capacite;
        self.contenu: list[Objet] = contenu;
    
    def fromCapacite(capacite: int):
        return Sac(capacite, []);

    def fromSac(sac):
        return Sac(sac.capacite, sac.contenu[:]);

    def evaluer(self) -> float:
        res = 0.;
        for objet in self.contenu:
            res += objet.valeur;
        return res;

    def ajouter(self, objet: Objet):
        self.contenu += [objet];
    
    def retirer(self, objet: Objet):
        self.contenu.remove(objet);

    def contient(self, objet: Objet) -> bool:
        return objet in self.contenu;

    def toggle(self, objet: Objet):
        if (self.contient(objet)):
            self.retirer(objet);
        else:
            self.ajouter(objet)

    def masseContenu(self) -> int:
        res = 0;
        for objet in self.contenu:
            res += objet.masse;
        return res;

    def estTropPlein(self) -> bool:
        return self.masseContenu() > self.capacite;

    def fixer(self):
        while(self.estTropPlein()):
            indice = random.randrange(len(self.contenu));
            objet = self.contenu[indice]
            self.retirer(objet);

    def __str__(self) -> str:
        res = "Sac:";
        for objet in self.contenu:
            res += "\n\t{}".format(objet);
        return res;
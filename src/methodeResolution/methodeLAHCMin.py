from methodeResolution.Methode import Methode
from probleme.Probleme import Probleme
from solution.Solution import Solution


class MethodeLAHCMin(Methode):
    def __init__(self, probleme: Probleme, tailleMem: int, nIter: int):
        self.probleme = probleme;
        self.tailleMem = tailleMem;
        self.nIter = nIter;

    def resoudre(self) -> Solution:
        candidat = self.probleme.candidat();
        valeurCandidat = candidat.evaluer();
        optimum = candidat;
        valeurMin = valeurCandidat;
        tabMemoire = [valeurMin for i in range(self.tailleMem)];
        for n in range(1, self.nIter):
            voisin = self.probleme.voisin(candidat);
            valMem = tabMemoire[n % self.tailleMem];
            if (valMem >= voisin.evaluer()):
                candidat = voisin;
            tabMemoire[n % self.tailleMem] = candidat.evaluer();
            if (valeurMin > voisin.evaluer()):
                optimum = voisin;
                valeurMin = voisin.evaluer();
        return optimum;

            
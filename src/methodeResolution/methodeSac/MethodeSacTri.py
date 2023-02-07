from methodeResolution.Methode import Methode
from outils.Objet import Objet
from solution.Sac import Sac


class MethodeSacTri(Methode):
    def resoudre(self) -> Sac:
        objets = self.probleme.getObjets();
        self.trier(objets)
        sac = self.probleme.candidat();
        for objet in objets:
            sac.ajouter(objet);
            if (sac.estTropPlein()):
                sac.retirer(objet);
        return sac;
    
    def trier(self, objets: list[Objet]):
        raise NotImplementedError;
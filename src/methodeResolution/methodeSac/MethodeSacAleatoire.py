import random
from methodeResolution.methodeSac.MethodeSacTri import MethodeSacTri
from outils.Objet import Objet
from probleme.Probleme import Probleme


class MethodeSacAleatoire(MethodeSacTri):
    def __init__(self, probleme: Probleme):
        self.probleme = probleme;
    
    def trier(self, objets: list[Objet]):
        random.shuffle(objets);
from outils.Point import Point


def lire(path: str) -> list[Point]:
    res = [];
    with open(path, "r") as fichier:
        line = fichier.readline();
        while line:
            infos = line.split(" ");
            yield infos;
            line = fichier.readline();
    fichier.close();

import math


class Point:
    def __init__(self, nom: str, x: float, y: float):
        self.nom: str = nom;
        self.x: float = x;
        self.y: float = y;

    def distance(self, other) -> float:
        dx = other.x - self.x;
        dy = other.y - self.y;
        return math.sqrt(dx * dx + dy * dy);
    
    def __str__(self) -> str:
        return "Point {}: {} ; {}"\
            .format(
                self.nom,
                self.x,
                self.y
            );

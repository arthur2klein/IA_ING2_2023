from __future__ import annotations
import math


class Point:
    """Point in a two-dimensional space.
    """
    def __init__(
        self,
        nom: str,
        x: float,
        y: float
    ):
        """Create a point in a two-dimensional space.

        Args:
            nom (str): Name of the point.
            x (float): X coordinate of the point.
            y (float): Y coordinate of the point.
        """
        self.nom: str = nom;
        self.x: float = x;
        self.y: float = y;

    def distance(self, other: Point) -> float:
        """Calculate the distance between the current particule and the given
        one.

        Args:
            other (Point): Particule to calculate the distance with.

        Returns:
            float: Distance between the two particules.
        """
        dx = other.x - self.x;
        dy = other.y - self.y;
        return math.sqrt(dx * dx + dy * dy);
    
    def __str__(self) -> str:
        """Create a string containing all the informations of the point.

        Returns:
            str: String containing all the informations of the point.
        """
        return f'Point {self.nom}: {self.x} ; {self.y}';
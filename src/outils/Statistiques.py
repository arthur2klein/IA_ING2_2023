from math import sqrt


class Statistiques:
    """Statistics about a set of data.
    """
    def __init__(self):
        """Initialize the statistics.
        """
        self.lValeurs: list[float] = [];

    def ajouter(self, valeur: float):
        """Add a new value to the date.

        Args:
            valeur (float): Value to add to the data.
        """
        self.lValeurs += [valeur];

    def min(self) -> float:
        """Calculate the minimum of the data of the instance.

        Returns:
            float: Minimum of the data of the instance.
        """
        return min(self.lValeurs);

    def max(self) -> float:
        """Calculate the maximum of the data of the instance.

        Returns:
            float: Maximum of the data of the instance.
        """
        return max(self.lValeurs);

    def percentile(self, position: float) -> float:
        """Calculate the given percentile of the data of the instance.

        Args:
            position (float): Index of the percentile to calculate.

        Returns:
            float: Nth percentile of the data to calculate.
        """
        self.lValeurs.sort();
        indice = position * len(self.lValeurs);
        indiceEntier = int(indice);
        indiceDecimal = indice - indiceEntier;
        return self.lValeurs[indiceEntier] * (1 - indiceDecimal) + \
               self.lValeurs[indiceEntier + 1] * indiceDecimal;

    def mediane(self) -> float:
        """Calculate the median of the data of the instance.

        Returns:
            float: Median of the data of the instance.
        """
        return self.percentile(position = 0.5);

    def moyenne(self) -> float:
        """Calculate the mean of the data of the instance.

        Returns:
            float: Mean of the data of the instance.
        """
        return sum(self.lValeurs) / len(self.lValeurs);

    def variance(self) -> float:
        """Calculate the variance of the data of the instance.

        Returns:
            float: Variance of the data of the instance.
        """
        moyenne = self.moyenne();
        return sum(
            valeur * valeur for valeur in self.lValeurs
        ) / len(self.lValeurs) - moyenne * moyenne;

    def ecartType(self) -> float:
        """Calculate the standard deviation of the data of the instance.

        Returns:
            float: Standard deviation of the data of the instance.
        """
        return sqrt(self.variance());
        
    def __str__(self) -> str:
        """Create a string containing most of the statistics about the data of
        the instance.

        Returns:
            str: String containing most of the statistics about the data of the
            instance.
        """
        return (
            f'Statistiques : \n'
            f'\tmediane    ={self.mediane():> 20,.5f}\n'
            f'\tmoyenne    ={self.moyenne():> 20,.5f}\n'
            f'\tmin        ={self.min():> 20,.5f}\n'
            f'\tmax        ={self.max():> 20,.5f}\n'
            f'\tecart type ={self.ecartType():> 20,.5f}'
        );
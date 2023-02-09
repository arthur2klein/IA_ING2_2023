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
        self.lValeurs.sort();

    def min(self) -> float:
        """Calculate the minimum of the data of the instance.

        Returns:
            float: Minimum of the data of the instance.
        """
        return self.lValeurs[0];

    def max(self) -> float:
        """Calculate the maximum of the data of the instance.

        Returns:
            float: Maximum of the data of the instance.
        """
        return self.lValeurs[-1];

    def percentile(self, position: float) -> float:
        """Calculate the given percentile of the data of the instance.

        Args:
            position (float): Index of the percentile to calculate.

        Returns:
            float: Nth percentile of the data to calculate.
        """
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
        return self.percentile(0.5);

    def moyenne(self) -> float:
        """Calculate the mean of the data of the instance.

        Returns:
            float: Mean of the data of the instance.
        """
        res = 0.;
        for valeur in self.lValeurs:
            res += valeur;
        return res / len(self.lValeurs);

    def variance(self) -> float:
        """Calculate the variance of the data of the instance.

        Returns:
            float: Variance of the data of the instance.
        """
        res = 0.;
        for valeur in self.lValeurs:
            res += valeur * valeur;
        moyenne = self.moyenne;
        return res / len(self.lValeurs) - moyenne() * moyenne();

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
        return "Statistiques : \n \
               min = {}\n\
               \tmax = {}\n\
               \tmoyenne = {}\n\
               \tmediane = {}\n\
               \tecart type = {}"\
               .format(self.min(),
                       self.max(),
                       self.moyenne(),
                       self.mediane(),
                       self.ecartType()
                    );
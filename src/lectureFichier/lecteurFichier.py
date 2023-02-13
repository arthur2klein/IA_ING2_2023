from typing import Generator


def lire(path: str) -> Generator[list[str], None, None]:
    """Read a file and generate an iterator of its lines as lists of words.

    Args:
        path (str): Path to the file from the root of the project.

    Yields:
        Iterator[list[Point]]: Generator iterating over the lines of the document
        and containing lists of words.
    """
    with open(path, "r") as fichier:
        line: str = fichier.readline();
        while line:
            infos: list[str] = line.split(sep = " ");
            yield infos;
            line = fichier.readline();
    fichier.close();

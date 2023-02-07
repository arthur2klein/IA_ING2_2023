import numpy
import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
from methodeResolution.MehodePCO import MethodePCO

from probleme.ProblemeEssaim import ProblemeEssaim, Topologie, rosenbrock

#pipenv run pip install pyswarms
def resolutionAvecPySwarms():
    options = {
        'c1': 1.47,
        'c2': 1.47,
        'w': 0.7
    };
    optimizer_10particules = ps.single.GlobalBestPSO(
        n_particles = 10,
        dimensions = 10,
        options = options,
        ftol = 1e-8
    );
    best_cost, best_pos = optimizer_10particules.optimize(fx.rosenbrock, iters = 1000);
    print("best_cost: {}\nbest_pos: {}".format(best_cost, best_pos));

    print("Comparaison:")
    probleme = ProblemeEssaim(
        rosenbrock,
        10,
        rosenbrock.borneInf,
        rosenbrock.borneSup,
        Topologie.tousMemeGroupe,
        10,
        0.7,
        1.47
    );
    methode = MethodePCO(probleme, 10000);
    solution = methode.resoudre();
    best_cost, best_pos = solution.evaluer(), solution.meilleurPos();
    print("best_cost: {}\nbest_pos: {}".format(best_cost, best_pos));

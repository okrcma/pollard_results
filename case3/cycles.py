from pollard.walk import *
from pollard.iter import *
from pollard.pollard_cycle import *
from measure.io import write_json
from pollard.curve_graph import *
import sage.all as sg
import json
import random

if __name__ == "__main__":
    BITS = 20

    gf_it = AllFieldsIterator(min_field_order=2**(BITS-1), max_field_order=2**BITS-1, prime_fields_only=True)
    gf = next(gf_it)
    # gf = sg.GF(1034644697)

    e_it = PrimeOrderCurvesIterator(RandomCurvesIterator(gf))
    e = next(e_it)
    # e = sg.EllipticCurve(gf, [88531777, 33507665])
    print(e)

    s = e.random_point()
    k = random.randint(0, s.order() - 1)
    t = k * s
    print("s:", s)
    print("k:", k)
    print("t:", t)
    # s = e(473, 355, 1)
    # t = e(15, 302, 1)

    x, y = gf["x", "y"].gens()
    p_s = x*y
    p_t = x+y
    print("p_s:", p_s)
    print("p_t:", p_t)
    g_s = PolynomialFunction(p_s, 2).eval
    g_t = PolynomialFunction(p_t, 2).eval
    # dim=2
    # p_it = RandomPolynomialsIterator(gf, max_degree=2, dim=dim)
    # p1 = next(p_it)
    # p2 = next(p_it)
    # p3 = next(p_it)
    # g_s = PolynomialFunction(p1, dim).eval
    # g_t = PolynomialFunction(p2, dim).eval
    # g_p = PolynomialFunction(p3, dim).eval

    # w = NonDeterministicRandomWalk(e)
    w = GeneralWalk(s=s, t=t, g_s=g_s, g_t=g_t)

    graph = CurveGraph.map_curve(e, w)

    # graph.show()

    print(json.dumps(graph.get_stats(), indent=2))

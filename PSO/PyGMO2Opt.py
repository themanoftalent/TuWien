import pygmo as pg


prob = pg.problem(pg.zdt(1))
algo = pg.algorithm(pg.nsga2())
pop = pg.population(prob, size=100)
pop = algo.evolve(pop)
res = pop.get_f()
print(res)

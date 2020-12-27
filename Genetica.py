import random
import numpy

def determination_of_suitability(equation_inputs, popul):
    suit = numpy.sum(popul * equation_inputs, axis=1)
    return suit

def def_best(popul, suitab, num_parents):
    parents = numpy.empty((num_parents, popul.shape[1]))
    for parent_num in range(num_parents):
        max_suitab_idx = numpy.where(suitab == numpy.max(suitab))
        max_suitab_idx = max_suitab_idx[0][0]
        parents[parent_num, :] = popul[max_suitab_idx, :]
        suitab[max_suitab_idx] = -99999999999
    return parents

def pairing(parents, child_c):
    childs = numpy.empty(child_c)
    pairing_point = numpy.uint8(child_c[1] / 2)
    for k in range(child_c[0]):
        parent1_idx = k%parents.shape[0]
        parent2_idx = (k+1)%parents.shape[0]
        childs[k, 0:pairing_point] = parents[parent1_idx, 0:pairing_point]
        childs[k, pairing_point:] = parents[parent2_idx, pairing_point:]
    return childs

def mutation(child_c):
    for idx in range(child_c.shape[0]):
        random_value = numpy.random.uniform(-1.0, 1.0, 1)
        child_c[idx, 4] = child_c[idx, 4] + random_value
    return child_c

equation_inputs = [random.randint(-20, 20) for i in range(7)]
num_weights, sol_per_pop, num_parents_mating, gen_n = 7, 9, 6, 5
pop_size = (sol_per_pop, num_weights)
new_pop = numpy.random.uniform(low=-4, high=4, size=pop_size)

for gen in range(gen_n):
    suit = determination_of_suitability(equation_inputs, new_pop)
    parents = def_best(new_pop, suit, num_parents_mating)
    childs = pairing(parents, child_c=(pop_size[0] - parents.shape[0], num_weights))
    muts = mutation(childs)
    new_pop[0:parents.shape[0], :] = parents
    new_pop[parents.shape[0]:, :] = muts

suit = determination_of_suitability(equation_inputs, new_pop)
best_match_idx = numpy.where(suit == numpy.max(suit))
print("Лучшее потомство : ", new_pop[best_match_idx, :])
print("Пригодность : ", suit[best_match_idx])
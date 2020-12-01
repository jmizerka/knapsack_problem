import numpy as np
import random
# create population function
def create_pop(number_of_individuals, genes):
    first_pop = np.zeros((number_of_individuals,genes),dtype = np.int8)
    for i in range(number_of_individuals):
        for j in range(genes):
            if random.randint(0,1) == 1:
                first_pop[i,j] = 1
    return first_pop
# crossover function
def crossover(population_of_survivors, chance_of_crossing_over):
    list_of_individuals = [i for i in range(len(population_of_survivors))]
    for i in range(int(len(population_of_survivors)/2)):
        parent1 = random.choice(list_of_individuals)
        list_of_individuals.remove(parent1)
        parent2 = random.choice(list_of_individuals)
        list_of_individuals.remove(parent2)
        random_number = random.random()
        if random_number < chance_of_crossing_over:
            crossing_point = random.randint(1,len(population_of_survivors)-1)
            population_of_survivors[parent1][crossing_point:] = population_of_survivors[parent2][crossing_point:]
            population_of_survivors[parent2][:crossing_point] = population_of_survivors[parent1][:crossing_point]
    return population_of_survivors
# mutation function
def mutate(population,chance_of_mutation):
    for i in range(len(population)):
            random_number = random.random()
            number_of_genes = len(population[i])
            if  random_number < chance_of_mutation:
                mutation_index = random.randint(0,number_of_genes-1)
                if population[i,mutation_index] == 0:
                    population[i,mutation_index] = 1
                else:
                    population[i,mutation_index] = 0
    return population


# import knapsack
knapsack_txt = np.genfromtxt(fname='knapsack_4.txt')
genes = int(knapsack_txt[0,1])
items = knapsack_txt[1:]
capacity = int(knapsack_txt[0,0])
number_of_individuals = 4
population = create_pop(number_of_individuals,genes)
print(crossover(population,0.8))
print(mutate(population, 0.02))

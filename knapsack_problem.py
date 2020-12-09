import numpy as np
# create population function
def create_pop(number_of_individuals, genes):
    first_pop = np.random.randint(2, size=(number_of_individuals, genes))
    return first_pop

# calculate weights and values
def calc_knapsack(items,new_population):
    value_weight = np.random.randint(1,size= (len(new_population),2))
    for i in range(len(new_population)):
        for j in range(len(new_population[0])):
            if new_population[i][j] == 1:
                value_weight[i][0] += items[j][0]
                value_weight[i][1] += items[j][1]
    return value_weight

# fitness function
def fitness(value_weight, capacity, last_best):
    best_value = 0
    best_in_pop = 0
    evaluation = np.random.randint(1,size= (len(value_weight),1))
    for i in range(len(value_weight)):
        if value_weight[i][0] > 0 and value_weight[i][1] <= capacity:
            evaluation[i] = value_weight[i][0]
        if evaluation[i]> last_best:
            last_best = evaluation[i]
            best_in_pop = evaluation[i]
        else:
            if evaluation[i] > best_in_pop:
                best_in_pop = evaluation[i]
    return evaluation, last_best, best_in_pop

# selection function
def tournament(population,rate):
    best = 0
    new_population = np.random.randint(1,size= (len(population),len(population[0])))
    for i in range(len(population)):
        tournament_group = []
        for j in range(int(round(len(population)*0.4,0))):
            random_number = np.random.randint(0,len(population)-1)
            tournament_group.append(random_number)
        index = np.where(rate == max(rate[tournament_group]))
        new_population[i] = population[index[0][0]]
    return new_population

# crossover function
def crossover(population_of_survivors, chance_of_crossing_over):
    list_of_individuals = [i for i in range(len(population_of_survivors))]
    for i in range(int(len(population_of_survivors)/2)):
        parent1 = np.random.choice(list_of_individuals)
        list_of_individuals.remove(parent1)
        parent2 = np.random.choice(list_of_individuals)
        list_of_individuals.remove(parent2)
        random_number = np.random.random()
        if random_number < chance_of_crossing_over:
            crossing_point = np.random.randint(1,len(population_of_survivors)-1)
            tmp = population_of_survivors[parent1].copy()
            population_of_survivors[parent1][crossing_point:] = population_of_survivors[parent2][crossing_point:]
            population_of_survivors[parent2][crossing_point:] = tmp[crossing_point:]
    return population_of_survivors

# mutation function
def mutate(crossed_population,chance_of_mutation):
    for i in range(len(crossed_population)):
            random_number = np.random.random()
            number_of_genes = len(crossed_population[i])
            if  random_number < chance_of_mutation:
                mutation_index = np.random.randint(0,number_of_genes-1)
                if crossed_population[i,mutation_index] == 0:
                    crossed_population[i,mutation_index] = 1
                else:
                    crossed_population[i,mutation_index] = 0
    return crossed_population

# import knapsack
knapsack_txt = np.genfromtxt(fname='knapsack_4.txt')
genes = int(knapsack_txt[0,1])
items = knapsack_txt[1:]
capacity = int(knapsack_txt[0,0])
number_of_individuals = 4
chance_of_crossing_over = 0.9
chance_of_mutation = 0.02

population = create_pop(number_of_individuals,genes)
value_weight = calc_knapsack(items,population)
rate,best_of_all, best_in_pop = fitness(value_weight,capacity,8)
next_pop = tournament(population,rate)
crossed_pop = crossover(next_pop.copy(),chance_of_crossing_over)
mutated_pop = mutate(crossed_pop.copy(),chance_of_mutation)
print(population)
print(value_weight)
print(rate)
print(next_pop)
print(crossed_pop)
print(mutated_pop)
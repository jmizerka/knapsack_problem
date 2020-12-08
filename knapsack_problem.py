import numpy as np
import random

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
def fitness(value_weight, capacity, population, last_best):
    best_value = 0
    best_individual = 0
    for i in range(len(value_weight)):
        if value_weight[i][0] > best_value and value_weight[i][1] <= capacity:
            best_individual = i
            best_value = value_weight[i][0]
        if last_best < best_individual:
            last_best = best_individual
    return best_individual,best_value

# selection function
def tournament(population,value_weight,capacity):
    tournament_groups = []
    winner = []
    best = 0
    new_population = np.random.randint(1,size= (len(population),len(population[0])))
    for i in range(len(population)):
        temp_list = []
        for j in range(2):
            while True:
                random_number = random.randint(1,len(population))
                if value_weight[random_number-1][1] <= capacity:
                    break
            temp_list.append(random_number-1)
        tournament_groups.append(temp_list)
    for i in range(len(tournament_groups)):
        if value_weight[tournament_groups[i][0]][0] > value_weight[tournament_groups[i][1]][0]:
            best = tournament_groups[i][0]
        else:
            best = tournament_groups[i][1]
        winner.append(best)
    for i in range(len(population)):
        new_population[i] = population[winner[i]]
    return new_population

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
def mutate(crossed_population,chance_of_mutation):
    for i in range(len(crossed_population)):
            random_number = random.random()
            number_of_genes = len(crossed_population[i])
            if  random_number < chance_of_mutation:
                mutation_index = random.randint(0,number_of_genes-1)
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
previous_best = 0

population = create_pop(number_of_individuals,genes)
value_weight = calc_knapsack(items,population)
best_ind,best_val = fitness(value_weight,capacity,population, previous_best)
next_pop = tournament(population,value_weight,capacity)

print(population)
print(value_weight)
print(next_pop)

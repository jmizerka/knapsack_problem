import numpy as np
import pygame


# create population function
def create_pop(number_of_individuals, genes):
    first_pop = np.random.randint(2, size=(number_of_individuals, genes))
    return first_pop


# calculate weights and values
def calc_knapsack(items, new_population):
    value_weight = np.random.randint(1, size=(len(new_population), 2))
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
    evaluation = np.random.randint(1, size=(len(value_weight), 1))
    for i in range(len(value_weight)):
        if value_weight[i][0] > 0 and value_weight[i][1] <= capacity:
            evaluation[i] = value_weight[i][0]
        if evaluation[i] > last_best:
            last_best = evaluation[i].item()
            best_in_pop = evaluation[i].item()
        else:
            if evaluation[i] > best_in_pop:
                best_in_pop = evaluation[i].item()

    return evaluation, last_best, best_in_pop


# selection function
def tournament(population, rate):
    new_pop = np.random.randint(1, size=(len(population), len(population[0])))
    for i in range(len(population)):
        tournament_group = []
        for j in range(int(round(len(population)*0.4, 0))):
            random_number = np.random.randint(0, len(population)-1)
            if len(tournament_group) > 0:
                if rate[tournament_group[0]] < rate[random_number]:
                    tournament_group.pop()
                    tournament_group.append(random_number)
            else:
                tournament_group.append(random_number)
        new_pop[i] = population[tournament_group[0]]
    return new_pop


# crossover function
def crossover(pop_of_winners, chance_of_crossing_over):
    list_of_individuals = [i for i in range(len(pop_of_winners))]
    for i in range(int(len(pop_of_winners)/2)):
        par1 = np.random.choice(list_of_individuals)
        list_of_individuals.remove(par1)
        par2 = np.random.choice(list_of_individuals)
        list_of_individuals.remove(par2)
        random_number = np.random.random()
        if random_number < chance_of_crossing_over:
            cross_pt = np.random.randint(1, len(pop_of_winners)-1)
            tmp = pop_of_winners[par1].copy()
            pop_of_winners[par1][cross_pt:] = pop_of_winners[par2][cross_pt:]
            pop_of_winners[par2][cross_pt:] = tmp[cross_pt:]
    return pop_of_winners


# mutation function
def mutate(crossed_population, chance_of_mutation):
    for i in range(len(crossed_population)):
            random_number = np.random.random()
            number_of_genes = len(crossed_population[i])
            if random_number < chance_of_mutation:
                num_of_mutations = np.random.randint(1,number_of_genes-1)
                for i in range(num_of_mutations):
                    mutation_index = np.random.randint(0, number_of_genes-1)
                if crossed_population[i, mutation_index] == 0:
                    crossed_population[i, mutation_index] = 1
                else:
                    crossed_population[i, mutation_index] = 0
    return crossed_population


def info():
    screen.fill(BLACK)
    info1 = font.render("Number of individuals: " + str(number_of_individuals),
                        True, WHITE)
    info2 = font.render("Chance of crossing-over: " +
                        str(chance_of_crossing_over), True, WHITE)
    info3 = font.render("Chance of mutation: " +
                        str(chance_of_mutation), True, WHITE)
    info4 = font.render("Best individual in population: " +
                        str(best_in_pop), True, WHITE)
    info5 = font.render("Best of all individuals: " +
                        str(best_of_all), True, WHITE)
    info6 = font.render("Press SPACE to start", True, WHITE)

    screen.blit(info2, (50, (10 + info1.get_height())))
    screen.blit(info3, (50, (20 + info1.get_height()*2)))
    screen.blit(info4, (470, (10 + info1.get_height())))
    screen.blit(info5, (470, (20 + info1.get_height()*2)))
    screen.blit(info6, (300, 125))


def visualization(rate):
    pygame.draw.line(screen, YELLOW, (0, 300), (800, 300), 5)
    ind_x = 30
    info8 = font.render("- rate >= 138000", True, WHITE)
    info9 = font.render("- rate < 138000", True, WHITE)
    info10 = font.render("- 138000 treshold", True, WHITE)
    screen.blit(info8, (320, 200))
    screen.blit(info9, (320, 225))
    screen.blit(info10, (320, 250))
    pygame.draw.rect(screen, GREEN, (300, 207, 10, 10))
    pygame.draw.rect(screen, WHITE, (300, 232, 10, 10))
    pygame.draw.rect(screen, YELLOW, (300, 257, 10, 10))

    for i in range(number_of_individuals):
        end_y = 800 - (rate[i][0] / (140000/500))
        if rate[i][0] >= 138000:
            pygame.draw.line(screen, GREEN, (ind_x, 800), (ind_x, end_y), 10)
        else:
            pygame.draw.line(screen, WHITE, (ind_x, 800), (ind_x, end_y), 10)
        ind_x += 15
    pygame.display.flip()
    pygame.display.update()


# import knapsack
knapsack_txt = np.genfromtxt(fname='ks_50_0')
genes = int(knapsack_txt[0, 0])
items = knapsack_txt[1:]
capacity = int(knapsack_txt[0, 1])
number_of_individuals = 50
chance_of_crossing_over = 0.9
chance_of_mutation = 0.01
initial_population = create_pop(number_of_individuals, genes)
best_of_all = 0
num_of_iter = 0
best_in_pop = 0
population = initial_population


# pygame
pygame.init()
SCREEN_SIZE = (800, 800)
screen = pygame.display.set_mode(SCREEN_SIZE)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 100, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
font = pygame.font.SysFont('times new roman', 18, WHITE)
clock = pygame.time.Clock()
pygame.display.set_caption("Genetic Algorithm")
info()
pygame.display.flip()
pygame.display.update()
while True:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
            if event.key == pygame.K_SPACE:
                for i in range(1000):
                    value_weight = calc_knapsack(items, population)
                    rate, best_of_all, best_in_pop = fitness(value_weight,
                                                             capacity,
                                                             best_of_all)
                    next_pop = tournament(population.copy(), rate.copy())
                    crossed_pop = crossover(next_pop.copy(),
                                            chance_of_crossing_over)
                    population = mutate(crossed_pop.copy(), chance_of_mutation)
                    print("Najlepszy w populacji to: ", best_in_pop)
                    info()
                    visualization(rate)
                    pygame.display.flip()
                    pygame.display.update()

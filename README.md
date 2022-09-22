# Knapsack Problem

# Description

This project was created for a class on artificial intelligence and artificial life. The main goal of the project was to solve an optimization problem known as the knapsack problem and visualize it. 

The main idea of the problem goes as follows: we have a given set of elements, each of which has a certain weight and value, and the goal is to determine which elements of the set to put in the "backpack" so that the sum of the weights is less than or equal to a given limit, and the value of the attached elements is as high as possible.

To achieve this goal genetic algorithm was used. This algorithm is inspired by natural selection of organisms. Firstly we have to initialize starting population, which is representing different possible solutions of a given problem in terms of "genetic code". Next fitness of each individual is evaluated and their are compared against each other by different methods. Winning individuals can be then subjected to crossing over and mutation and their fitness is evaluated again. The process continues until we get desired result. 

The program is written in Python language based on numpy and pygame libraries. 

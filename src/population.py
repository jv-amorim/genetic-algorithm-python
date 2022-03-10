import numpy as np
from config import INDIVIDUAL_LENGTH, POPULATION_SIZE
from individual import generate_random_individual


def generate_initial_population():
  population = np.empty((POPULATION_SIZE, INDIVIDUAL_LENGTH), np.ubyte)

  for i in range(0, POPULATION_SIZE):
    population[i] = generate_random_individual()

  return population


def get_individuals_to_the_next_generation(current_population, population_children):
  raise ValueError('Implementation missing.')

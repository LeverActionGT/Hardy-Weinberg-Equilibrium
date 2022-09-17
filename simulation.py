import random

import population
import individual

# create a simulation
class Simulation:
    def __init__(self, settings, fitness):
        self.settings = settings
        self.fitness = fitness
        self.pop = population.Population(self.settings['pop_size'])
        self.generation = 0
        self.data = {}
        self.create_initial_generation()
        
    # record the stats for the current generation
    def record_stats(self):
        # get the population stats
        stats = self.pop.get_stats()
        self.data[self.generation] = stats
        

    # create the initial generation
    def create_initial_generation(self):
        for i in range(self.settings['pop_size']):
            genes = random.choices(['A', 'a'], weights=[self.settings['initial_p'], self.settings['initial_q']], k=2)
            ind = individual.Individual(genes)
            self.pop.add(ind)
        self.record_stats()
        print('Initial Generation Created')

    # run the simulation
    def run_simulation(self):
        for i in range(self.settings['num_generations']):
            self.generation += 1
            next_generation = self.pop.next_generation(self.fitness)
            if self.pop.size < 2:
                print(f'Population too small to reproduce at generation {self.generation}')
                break
            self.pop = next_generation
            print(f'Generation {self.generation} created')
            self.record_stats()

        # Simulation Complete
        print('Simulation Complete')
        return self.data


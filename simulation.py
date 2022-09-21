import random

# create a simulation
class Simulation:
    def __init__(self, settings, fitness):
        self.settings = settings
        self.fitness = fitness
        self.data = {}
        self.create_initial_generation()

    # get the stats for the current generation
    def get_stats(self):
        p = self.genepool.count('A')/len(self.genepool)
        q = self.genepool.count('a')/len(self.genepool)
        return {
            'p': round(p, 4),
            'q': round(q, 4),
            'p2': round(p*p, 4),
            'q2': round(q*q, 4),
            '2pq': round(2*p*q, 4)
        }
        
    # create the initial generation    
    def create_initial_generation(self):
        self.generation = 0
        A_alleles = round(self.settings['initial_p']*self.settings['pop_size'])
        a_alleles = round(self.settings['initial_q']*self.settings['pop_size'])
        self.genepool = ['A']*A_alleles + ['a']*a_alleles

        # Record data for initial generation
        self.data[self.generation] = self.get_stats()
        self.print_stats(self.data[self.generation])

    # reproduce the current generation
    def reproduce(self):
        new_genepool = []
        kids = []

        # create the next generation by randomly selecting parents
        while len(kids) < self.settings['pop_size']:
            mama = random.choice(self.genepool)
            papa = random.choice(self.genepool)
            kid = mama + papa
            kids.append(kid)

        # apply fitness to the next generation & add to the new genepool
        for kid in kids:
            if kid == 'AA':
                if random.random() < self.fitness['AA_fitness']:
                    new_genepool.append('A')
                    new_genepool.append('A')
            elif kid == 'Aa' or kid == 'aA':
                if random.random() < self.fitness['Aa_fitness']:
                    new_genepool.append('A')
                    new_genepool.append('a')
            elif kid == 'aa':
                if random.random() < self.fitness['aa_fitness']:
                    new_genepool.append('a')
                    new_genepool.append('a')
        return new_genepool

    # print stats
    def print_stats(self, stats):
        if self.settings['print_stats']:
            print(
                'Generation' + str(self.generation) + ':',
                '\tp: ' + str(stats['p']),
                '\tq: ' + str(stats['q']),
                '\tp^2: ' + str(stats['p2']),
                '\tq^2: ' + str(stats['q2']),
                '\t2pq: ' + str(stats['2pq'])
            )

    # run the simulation
    def run_simulation(self):
        for i in range(self.settings['num_generations']):
            self.generation += 1
            self.genepool = self.reproduce()
            self.data[self.generation] = self.get_stats()
            self.print_stats(self.data[self.generation])

            # stop if an allele is extinct
            if self.data[self.generation]['p'] == 0:
                print(f' \nAllele A has gone extinct on generation {self.generation}!')
                break
            if self.data[self.generation]['q'] == 0:
                print(f' \nAllele a has gone extinct on generation {self.generation}!')
                break

        # done
        print(' \nSimulation complete!')

        # report initial conditions
        print(f' \nInitial Conditions:\n\tp: {self.settings["initial_p"]}\n\tq: {self.settings["initial_q"]}\n\nFitness:\n\tAA_fitness: {self.fitness["AA_fitness"]}\n\tAa_fitness: {self.fitness["Aa_fitness"]}\n\taa_fitness: {self.fitness["aa_fitness"]}')
        return self.data
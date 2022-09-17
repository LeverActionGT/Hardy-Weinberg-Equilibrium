import random
import math
import individual


# a population of individuals

class Population:
    def __init__(self, size:int):
        self.size = size
        self.members = []
        self.reproductive_size = self.size

    def __str__(self):
        pop_members = []
        for member in self.members:
            pop_members.append(member.gene())
        return 'Population of size ' + str(self.size) + '\n' + str(pop_members)

    # add an individual to the population
    def add(self, member:individual.Individual):
        self.members.append(member)

    def natural_selection(self, fitness:dict):
        for member in self.members:
            # get the fitness of the individual
            if member.gene() == 'AA':
                member_fitness = fitness['AA_fitness']
            elif member.gene() == 'Aa' or member.gene() == 'aA':
                member_fitness = fitness['Aa_fitness']
            elif member.gene() == 'aa':
                member_fitness = fitness['aa_fitness']
            
            # kill individuals according to fitness
            for member in list(self.members):
                if random.uniform(0, 1) > member_fitness:
                    self.members.remove(member)

    # return the next generation of individuals
    def next_generation(self, fitness:dict):
        # natural selection
        self.natural_selection(fitness)
        self.reproductive_size = len(self.members)
        # if the population is too small to reproduce, return the current population
        if len(self.members) < 2: return self

        # create the next generation
        next_gen = Population(self.size)
        for i in range(self.size):
            # pick two random individuals
            parents = random.sample(self.members, 2)

            child_genes = []
            for parent in parents:
                # pick a random gene from the parent
                gene = random.choice(parent.genes)

                # add the gene to the child
                child_genes.append(gene)

            # add the child to the next generation
            child = individual.Individual(child_genes)
            next_gen.add(child)
        return next_gen

    # get the population stats
    def get_stats(self):
        AA = 0
        Aa = 0
        aa = 0
        for member in self.members:
            if member.gene() == 'AA':
                AA += 1
            elif member.gene() == 'Aa' or member.gene() == 'aA':
                Aa += 1
            elif member.gene() == 'aa':
                aa += 1
        
        p2 = AA / self.size
        q2 = aa / self.size
        p = math.sqrt(p2)
        q = math.sqrt(q2)

        stats = {
            'size': self.reproductive_size,
            'p': p,
            'q': q,
            'p2': p2,
            'q2': q2,
            '2pq': 2 * p * q,
        }
        return stats
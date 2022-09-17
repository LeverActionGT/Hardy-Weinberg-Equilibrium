# an individual in the population

class Individual:
    def __init__(self, genes:list):
        self.genes = genes # a list of two genes (A or a)

    def gene(self) -> str: # returns the gene in AA, Aa, aa format
        return f'{self.genes[0]}{self.genes[1]}'

    def __str__(self):
        return 'Individual with gene:' + self.gene()
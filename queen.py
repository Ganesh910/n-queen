import numpy as np

class nqueen:

    def __init__(self, n) -> None:
        self.n = n
        self.population = None

    def populate(self, times):
        """
        It creates a poplution of random places (chromosome) for queens in each column"""

        self.population = np.random.randint(1, self.n+1, size=(times, self.n))

    def fitness(self):
        """
        It will calculate the fitness in percentage for each chromosome.
        """
        mxm = ((self.n-1)*self.n)//2
        mnm = 0

    def selection():
        """
        For producing the next generation, it will create parents on the basis of fitness and probability and will also select the crossing over point.
        """

    def crossover():
        """
        The actual process of crossing over will be performed here."""

    def mutation():
        """"
        Some random mutation would be applied to the populations anologous to the evolution.
        """

q = nqueen(8)
q.populate(5)
print(q.population)
import numpy as np

class nqueen:

    def __init__(self, n) -> None:
        self.n = n
        self.population = None

    def populate(self, times):
        """
        It creates a poplution of random places (chromosome) for queens in each column"""

        self.population = np.random.randint(0, self.n, size=(times, self.n))

    def fitness(self):
        """
        It will calculate the fitness in percentage for each chromosome.
        """
        mxm = ((self.n-1)*self.n)//2 # maximum number of non attacking pairs possible
        mnm = 0
        fit = []
        fit_perecent=[]
        for ind1, pop in enumerate(self.population):
            pair=0
            for i in range(len(pop)):
                for j in range(i+1, len(pop)):
                    if not self.check_attack((pop[i], i), (pop[j], j)):
                        pair+=1
            fit.append(pair)

        total = sum(fit)
        
        for i in range(self.population.shape[0]):
            fit_perecent.append(round(fit[i]/total, 2))
        
        print("fit percent", fit_perecent)
        print("fit", fit)
                    
                
    def check_attack(self, cord1, cord2):
        """
        returns True if pair are attacking each other else False
        """

        if cord1[0]==cord2[0]:
            return True

        if abs(cord1[0]-cord2[0])==abs(cord1[1]-cord2[1]):
            return True
        
        return False

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

q = nqueen(4)
q.populate(6)
print(q.population)
q.fitness()
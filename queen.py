import random
import numpy as np

class ExitLoop(Exception):
    pass

class nqueen:
    def __init__(self, n) -> None:
        self.n = n
        self.population = None
        self.no_of_chromosomes=50 #Change the value accordingly as keep the number even else code might not behave as expected

    def populate(self):
        """It creates a poplution of random places (chromosome) for queens in each column.
        We will be taking even number for population for easy crossing over. (Won't create any differnce in working of This algo.)"""

        self.population = np.random.randint(0, self.n, size=(self.no_of_chromosomes, self.n))

    def fitness(self):
        """It will calculate the fitness in percentage for each chromosome."""
        mxm = ((self.n-1)*self.n)//2 # maximum number of non attacking pairs possible
        fit = []
        fit_perecent=[]
        for ind1, pop in enumerate(self.population): #iterate over each chromosome
            pair=0

            #nested for loop to iterate over each value of chromosome and do comparisons with each pair possible.
            for i in range(len(pop)):
                for j in range(i+1, len(pop)):

                    # If a pair of queen is not attacking each other then + 1
                    if not self.check_attack((pop[i], i), (pop[j], j)):
                        pair+=1
            if pair==mxm:

                print("Here is the answer:--------------------\n", self.population[ind1])
                raise ExitLoop
            fit.append(pair)

        total = sum(fit)
        
        for i in range(self.no_of_chromosomes):
            fit_perecent.append(round(fit[i]*100/total, 2))

        return fit_perecent
                    
                
    def check_attack(self, cord1, cord2):
        """
        returns True if pair are attacking each other else False
        """

        # if queens in same row
        if cord1[0]==cord2[0]:
            return True

        #if queens in same diagonal
        if abs(cord1[0]-cord2[0])==abs(cord1[1]-cord2[1]):
            return True
        
        return False

    def selection(self):
        """For producing the next generation, it will create parents on the basis of fitness and probability and will also select the crossing over point."""
        selected = random.choices(np.arange(0, self.no_of_chromosomes), self.fitness(), k=self.no_of_chromosomes)
        d={}
        for i in selected:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        return selected


    def crossover(self):
        """The actual process of crossing over will be performed here."""
        new_pop = np.empty((self.no_of_chromosomes, self.n), dtype=int)
        sel = self.selection()
        for i in range(0, len(sel), 2):
            point = random.randint(1, self.n-1)
            for j in range(0, point):
                new_pop[i][j] = self.population[sel[i]][j]
                new_pop[i+1][j] = self.population[sel[i+1]][j]
            for j in range(point, self.n):
                new_pop[i][j] = self.population[sel[i+1]][j]
                new_pop[i+1][j] = self.population[sel[i]][j]
        self.population = new_pop
        


    def mutation(self):
        """"Some random mutation would be applied to the populations anologous to the evolution."""
        for chrom in self.population:
            place = random.randint(0, self.n-1)
            val = random.randint(0, self.n-1)
            chrom[place] = val

    def generation(self, gen):
        """This function would be responsible for generations of the population"""
        for i in range(gen):
            try:
                self.crossover()
            except ExitLoop:
                print(str(i)+"th gen")
                exit()
            self.mutation()

q = nqueen(6)
q.populate()
q.generation(10000) #Choose number of generations accordinly, way too large number may take long time to execute

"""This program solves the n-queens problem by using genetic algorithm approach(which is a np-complete problem)so it doesn't use brute force
   there are several steps followed in the genetic algorithm
   1. Population - the method populate creates a large no of chromosomes by placing one queen randomly in the array(chromosome)
   2. Fitness - Number of non attacking pairs in a chromosome is calculated
   3. Selection - Only the fittest chromosomes are selected
   4. Crossover - chromosomes are crossed over to create the fittest pairs possible
   5. Mutation - Some random genes are changed in the chromosomes to create a new diversity of chromosomes(solution)
   Finally it combines the best of the best solutions to form a best single solution
"""

import random
import numpy as np


class ExitLoop(Exception):
    pass
    """
    Raises:
        ExitLoop

    Returns:
        None
    """    

class nqueen:
    def __init__(self, n) -> None:
        self.n = n
        self.population = None
        # Change the value accordingly as keep the number even else code might not behave as expected
        self.no_of_chromosomes = 50


    def populate(self):   
        """It creates a population of random places (chromosome) for queens in each column.
        We will be taking even number for population for easy crossing over. (Won't create any differnce in working of This algo.)"""

        self.population = np.random.randint(
            0, self.n, size=(self.no_of_chromosomes, self.n))

    def fitness(self):
        """It will calculate the fitness in percentage for each chromosome."""
        mxm = ((self.n-1)*self.n)//2  # maximum number of non attacking pairs possible
        fit = []
        fit_perecent = []
        # iterate over each chromosome
        for ind1, pop in enumerate(self.population):
            pair = 0
            
            # nested for loop to iterate over each value of chromosome and do comparisons with each pair possible.
            for i in range(len(pop)):
                for j in range(i+1, len(pop)):

                    # If a pair of queen is not attacking each other then + 1
                    if not self.check_attack((pop[i], i), (pop[j], j)):
                        pair += 1
            if pair == mxm:

                print("Here is the answer:--------------------\n",
                      self.population[ind1])
                raise ExitLoop
            fit.append(pair)

        total = sum(fit)
        
        fit_perecent = [round((fit[i]*100/total), 2)
                        for i in range(self.no_of_chromosomes)]
        return fit_perecent

    def check_attack(self, cord1, cord2):
        """
        returns True if pair are attacking each other else False
        """

        # if queens in same row
        if cord1[0] == cord2[0]:
            return True

        # if queens in same diagonal
        if abs(cord1[0]-cord2[0]) == abs(cord1[1]-cord2[1]):
            return True

        return False

    def selection(self):
        """For producing the next generation, it will create parents on the basis of fitness and probability and will also select the crossing over point."""
        selected = random.choices(
            np.arange(0, self.no_of_chromosomes), self.fitness(), k=self.no_of_chromosomes)
        d = {}
        for i in selected:  # iterating through every chromosome
            if i not in d:  # if the chromosome is fit , it is selected
                d[i] = 1
            else:
                d[i] += 1
        return selected

    def crossover(self):
        """The actual process of crossing over will be performed here."""
        new_pop = np.empty((self.no_of_chromosomes, self.n), dtype=int)
        sel = self.selection()
        for i in range(0, len(sel), 2):
            # crossing of the genes at random points
            point = random.randint(1, self.n-1)

            # Used List Slicing techniques here
            new_pop[i][:point] = self.population[sel[i]][:point]
            new_pop[i+1][:point] = self.population[sel[i+1]][:point]
            new_pop[i][point:] = self.population[sel[i+1]][point:]
            new_pop[i+1][point:] = self.population[sel[i]][point:]
        self.population = new_pop

    def mutation(self):
        """"Some random mutation would be applied to the populations analogous to the evolution."""
        for chrom in self.population:
            place = random.randint(0, self.n-1)
            val = random.randint(0, self.n-1)
            chrom[place] = val  # random mutation taking place

    def generation(self, gen):
        """This function would be responsible for generations of the population"""
        for i in range(gen):
            try:
                self.crossover()  # creating 100000 generations of correct solutions
            except ExitLoop:  # if an error occurs , it stops the generation showing that it has got the best solution
                print(str(i)+"th gen")
                exit()
            self.mutation()
        
    def backtrack():
        """
        Function returns sinlge bruteforce solution.
        """
        ...
    
    def findAll():
        """
        Function returns set of all solutions to the problem.
        """
        ...


q = nqueen(6)  # 6 queens should be placed in 6X6 chessboard
q.populate()
# Choose number of generations accordingly, way too large number may take long time to execute
q.generation(10000)

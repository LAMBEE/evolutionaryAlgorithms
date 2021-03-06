import numpy as np
import random
import string

# Calculate himmelblau, allele 0 and 1 == x and y respectively. 
def himmelblau(parent):
    x = parent[0]
    y = parent[1]
    return (x**2+y-11)**2 + (x+y**2-7)**2


# variables
problemName = 'Himmelblau minimization'
muSize = 15
lambdaSize = 100
mutationStdDev = .1
crossoverRate = .5
mutationRate = .5

# create header
print('<' + problemName + '>', '<' + str(muSize) + '>', '<' + str(lambdaSize) + '>','<' + str(mutationStdDev) + '>','<' + str(crossoverRate) + '>')


# generate solutions
initPop = []
for i in range(muSize):
    initPop.append((random.uniform(-10, 10), # generates random x and y values and the strategy values for each
                    random.uniform(-10, 10),
                    mutationStdDev, mutationStdDev))

# recombination
# I chose to use intermediate recombination because i believe it
# does a better job of focusing in a solution by averaging two parents together.
def recombination(parent1, parent2): # two parents go in
    child = [] # pre initializing array
    for i in range(4): # 4 alleles to act on
        a = random.uniform(0, 1) # random alpha coefficient
        child.append((a*parent1[i] + (1-a)*parent2[i])) # formula for intermidiate averaging
    return child

# mutation
# normal distribution / gaussian pertubation mean zero with variable stdDev to mutate genes
def mutation(parent):
    return [parent[0]+np.random.normal(0, parent[2]), parent[1]+np.random.normal(0, parent[3]), parent[2], parent[3]]
    # adds result of the normal distribution function unique for each x and y



# uniform random parent selection
def randParent(population):
    return population[random.randint(0, len(population)-1)]
# returns uniformly random chosen # mutation


# This function creates offspring pool and survivors all in 1
def survivorSelection():
    ###############################
    # First generate offspring pool
    offspring = []
    fitness = []
    count = 0
    while count < lambdaSize: # iterates lamda time to create offspring pool size
        if random.uniform(0, 1) <= crossoverRate: # crossover chance
            offspring.append(recombination(randParent(initPop), randParent(initPop)))
            count += 1
        elif random.uniform(0, 1) <= mutationRate: # mutation chance
            offspring.append(mutation(randParent(initPop)))
            count += 1
        else: # parent moves to offspring pool
            offspring.append(randParent(initPop))
            count += 1
    # end of offspring generation
    #############################

    #############################
    # Start of survivor selection
    for i in range(len(offspring)): 
        fitness.append(himmelblau(offspring[i])) # apply fitness function to each offspring
                                                    # and store values in fitness array
    mostFit = min(fitness) # find most fit individual
    avgFit = np.mean(fitness) # find average fitness of offspring
    newPop = []
    key = np.argpartition(fitness, muSize) # finds index of mu most fit solutions
    for i in range(muSize):
        newPop.append(offspring[key[i]]) # since index of fitness and offspring is the same this appends mu size offspring into new pop / survivors
        # based off their index. It essentially looks at fitness array to capture mu best offspring without sorting.
    return newPop, mostFit, avgFit
    # end of survivor selection
    ###########################

# MAIN #
generation = 1
for x in range(30):
    initPop, mostFit, avgFit = survivorSelection()
    print('<' + str(generation) + '>', '<' + str(mostFit) + '>', '<' + str(avgFit) + '>')
    generation += 1
    
    
    
    

    

    

            
       
        

    

# Liam Mulcahy
import random
import string
import numpy as np



# Variables for editing
problemName = 'Max Ones'
populationSize = 100
bitstringGenomeLength = 16
mutationRate = 0.001
crossoverRate = 0.5
generationLimit = 1000


# create header
print('<' + problemName + '>', '<' + str(populationSize) + '>', '<' + str(bitstringGenomeLength) + '>','<' + str(mutationRate) + '>','<' + str(crossoverRate) + '>')

# generate one solution.
# function concatinates string of random 0 or 1 into desired genome length.
def genIndividual():
    
    individual = ""

    for i in range(bitstringGenomeLength):
        individual += str(random.randint(0, 1)) 
    return individual

# returns array of individual solutions of population size
def initPop():
    return [genIndividual() 
        for x in range(populationSize)]

# FITNESS FUNCTION
def fitnessScore(population):
    
    return [population[x].count('1') / bitstringGenomeLength # Returns num of 1 in each individual
        for x in range(populationSize)]

def weighted(score):
    return [x / sum(score) for x in score]


# Creates array of cumulutive sums. useful when using roulette
def prob(weightedScore):
    return np.cumsum(weightedScore)

#######################################
#ROULETTE WHEEL SELECTION, picks one parent from population pool. run as many times as you want your parent population to be
def roulette(population, probability):
    choice = random.uniform(0, 1)
    i = 0
    while True:
        if choice <= probability[i]:
            return population[i]
            break 
        i += 1
#######################################       
# parents = []
#for _ in range(populationSize):
    #parents.append(roulette())


####################################################################
# MUTATION FUNCTION
def mutation(parent, mutationRate): #takes in parent and mutationRate
    choice = random.uniform(0, 1) # generate random number for check
    i = 0
    temp = list(parent) # convert string into list so it can be iterated through
    temp2 = [int(x) for x in temp] # convert elements from str to int so ABS can be used
    for i in range(bitstringGenomeLength): # iterate parent
        if choice <= mutationRate: # compare random number with mutation rate
            temp2[i] = abs(temp2[i]-1) # if choice <= to rate, flip bit with abs[i]-1
            i += 1
        else:
            i += 1 # otherweise, dont flip and iterate
    temp3 = ''.join(str(e) for e in temp2) #join list of ints into single string
    return temp3 #return string of flipped bits.. mutation of 1 = all bits flip
#####################################################################
# mutants = []
#for i in range(populationSize):
	#mutants.append(mutation(initPop[i], 1))
#mutants


##################################################################
# CROSSOVER FUNCTION
# TAKES IN PARENT POOL AND CROSSOVER RATE
def crossover(parents, crossoverRate):
    children = [] # create empty list
    # rate = crossoverRate 
    x = 0 # parent index
    while x < len(parents)-1: # iterate through parent pool
        choice = random.uniform(0, 1) # gen random number
        if choice <= crossoverRate: # crossover event
            crossoverPoint = random.randint(1, bitstringGenomeLength-1) # choose point for crossover
            ch1 = parents[x][:crossoverPoint] + parents[x+1][crossoverPoint:] # swap ends
            ch2 = parents[x+1][:crossoverPoint] + parents[x][crossoverPoint:] # swap ends
            children = children + [ch1, ch2] # add children too children pool
        else:
            children = children + [parents[x], parents[x+1]] # parents didnt mate :( 
            
        x = x + 2 # iterate parent index

    return children # returns children pool
##################################################################


# TERMINATION FUNCTION edit termination conditions as you wish
def termination(averageFitness, generationLimit): # for functions where convergence may be difficult, you can make lower average fitness requirements to ~.99
    if averageFitness < 1.0 and generation < generationLimit:
        return False
    elif averageFitness == 1.0:
        print('Population has converged')
        return True
    elif generation == generationLimit:
        print('Generation limit reached')
        return True
    


        
# #### #
# MAIN #
# #### #
# program executes here
generation = 0
pop = initPop()
avg = 0
x = []
y = []
while termination(avg, generationLimit) == False:
    score = fitnessScore(pop)
    weight = weighted(score)
    probability = prob(weight)
    parents = []
    for _ in range(populationSize):
        parents.append(roulette(pop, probability))
    mutants = []
    for i in range(populationSize):
        mutants.append(mutation(crossover(parents, crossoverRate)[i], mutationRate))
    pop = mutants
    
    # variables for output
    generation = generation + 1
    avg = sum(score) / populationSize
    
    # find percent
    unique = []
    for ele in pop:
        if ele not in unique:
            unique.append(ele)
            percent = round((1 / (len(unique) / populationSize)) / populationSize * 100, 4)
    #
    print('<' + str(generation) + '>', '<' + str(max(score)) + '>', '<' + str(avg) + '>', '<' + str(percent) + '>')
    x.append(generation)
    y.append(avg)


        
    
    
           








        






    




    







    


    





  
    


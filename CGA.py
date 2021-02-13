# Basic CGA functions
# Liam Mulcahy
import random
import string
import numpy as np
import matplotlib.pyplot as plt

# Variables for editing
problemName = 'Max Ones'
populationSize = 20
bitstringGenomeLength = 10
mutationRate = 0.01
crossoverRate = 0.5

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
initPop = [genIndividual() 
        for x in range(populationSize)]

# assignes fitness score to each individual in population
def fitnessScore():
    
    return [initPop[x].count('1') / bitstringGenomeLength # Returns num of 1 in each individual
        for x in range(populationSize)]

weighted = [x / sum(fitnessScore()) for x in fitnessScore()]

# CUM SUM :P
# Creates array of cumulutive sums. useful when using roulette
prob = np.cumsum(weighted)

#pick one individual
def roulette():
    choice = random.uniform(0, 1)
    i = 0
    while True:
        if choice <= prob[i]:
            return initPop[i]
            break
        # comment in print if you wish to see it iterate for sanity sake
        # print(i) 
        i += 1
# parents = []
#for _ in range(populationSize//2):
    #parents.append(roulette())


#Teenage MUTANT nija turtles           
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
# mutants = []
#for i in range(populationSize):
	#mutants.append(mutation(initPop[i], 1))
#mutants

            
            
            
        
    
        
           









        






    




    







    


    





  
    


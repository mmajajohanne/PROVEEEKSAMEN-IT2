# https://www.youtube.com/watch?v=4XZoVQOt-0I

"""
Genetic algorithm is an algorithm that can solve problems with no clear 
solution by generating random solutions and picking the beat results then 
applying a crossover and a mutation to the best solutions before starting 
the process again. 
Key moments in the code:
* create a large list of random solutions (1000 in this case)
* pick the best (100 in this case)
* create a new list of solutions of random and mutated instances from the best picked out solutions 
* do it all again 

"""

import random


def foo(x, y, z):
    return 3*x**2 + 4*y + 5*z - 25 
    # Want function to be as close to 25 as possible (foo as close to 0 as possible)

def foo2(x, y, z):
    return 3*x**2 + 4*y + 5*z 

def fitness(x, y, z): #
    ans = foo(x, y, z) # stores foo result in ans 

    if ans == 0:
        return 999999

    else: 
        return abs(1/ans) # ranking system, returns bigger number for smaller ans (closer to 0)


# 1 - create large list of random solutions that is tuples with 3 random numbers 
solutions = []
for s in range(1000): 
    # Generate a tuple with a random instance of (x, y, z)
    solutions.append(   (   random.uniform(0, 10000),
                            random.uniform(0, 10000),
                            random.uniform(0, 10000)    )  )
    


for i in range(10000):

# 2 - rank all random solutions and sort by ranking 
    rankedsolutions = []
    for s in solutions: #for all random number tuples 
        rankedsolutions.append( (fitness(s[0], s[1], s[2]), s) ) # run fitness and return a ranking and the s-tuple used 

    #sort and reverse so that highest ranking comes first 
    rankedsolutions.sort()
    rankedsolutions.reverse()

    print(f"=== Gen{i} best solutions ===") # Header for the best ranked solutions in generation number i
    print(rankedsolutions[0]) #The best solution 

    # to stop the x, y, z, generations when ranking (fitness) is over a certain ranking
    if rankedsolutions[0][0] > 999:
        break

# 3 - Pick out a number of the best solutions 
    bestsolutions = rankedsolutions[:100] # Assign the 100 best ranked solutions to bestsolutions list 


    # create lists for each parameter x, y, z with all instances from bestsolutions  
    elements_x = []
    elements_y = []
    elements_z = []
    for s in bestsolutions: 
        # first parameter finds the tuple-instance, second parameter finds x, y or z
        elements_x.append(s[1][0])  
        elements_y.append(s[1][1])
        elements_z.append(s[1][2])

# 4 - create a new list with tuples of random, mutated instances of x, y, z 
    newGen = []
    for _ in range(1000):
        # Choose three random numbers from all x, y, z elements in elements list 
        e1 = random.choice(elements_x) * random.uniform(0.99, 1.01) # mutate all numbers by 2 % 
        e2 = random.choice(elements_y) * random.uniform(0.99, 1.01)
        e3 = random.choice(elements_z) * random.uniform(0.99, 1.01)

        newGen.append((e1, e2, e3))  
    
    solutions = newGen # assigning solutions to the new generated list 



# printing out results 
print(rankedsolutions[0])
print(foo2(rankedsolutions[0][1][0], rankedsolutions[0][1][1], rankedsolutions[0][1][2]))
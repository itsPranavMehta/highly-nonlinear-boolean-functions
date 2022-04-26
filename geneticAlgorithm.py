from numpy.random import rand
from numpy.random import randint
from sympy import fwht
import time
# genetic algorithm to search for Boolean variables with high nonlinearity.

THRESH_HOLD=0.98

def getScore(seq):
    # print(seq)
    # use_seq=seq
    use_seq = [i for i in seq]
    convert_to_polarised(use_seq)
    transform = fwht(use_seq)
    mx = max(abs(min(transform)), max(transform))
    # print('max: ',mx_non_linearity)
    # print('val: ', 2**(var-1)-mx/2)
    # if(mx_non_linearity == 2**(var-1)-mx/2):
    #     print('found: ', mx_non_linearity, 2**(var-1)-mx/2,seq)
    curr_non_linearity=2**(var-1)-mx/2
    return mx_non_linearity-curr_non_linearity
    #score =mx_non-curr_non
    #curr_non=mx_non-score
    #squared errors won't make a difference here....

def convert_from_polarised(seq):
    for i in range(0, len(seq)):
        if(seq[i] == -1):
            seq[i] = 1
        else:
            seq[i] = 0


def convert_to_polarised(seq):
    for i in range(0, len(seq)):
        if(seq[i]):
            seq[i] = -1
        else:
            seq[i] = 1


 
def selection(pop, scores, k=4):
    # first random selection
    selection_ix = randint(len(pop))
    for ix in randint(0, len(pop), k-1):
        # check if better (e.g. perform a tournament)
        if scores[ix] < scores[selection_ix]:
            selection_ix = ix
    return pop[selection_ix]

# crossover two parents to create two children

def crossover(p1, p2, r_cross):     #one point crossover 
    # children are copies of parents by default
    child1, child2 = p1.copy(), p2.copy()
    # check for recombination
    if rand() < r_cross:
        # select crossover point that is not on the end of the string
        pt = randint(1, len(p1)-2)
        # perform crossover
        child1 = p1[:pt] + p2[pt:]
        child2 = p2[:pt] + p1[pt:]
    return [child1, child2]

def twoPointCrosover(p1,p2,r_cross):

    child1,child2=p1.copy(),p2.copy()
    #use only if the rate of crossover is greater than the random value generated
    if rand()<r_cross:
        pt1=randint(1,len(p1)-4)
        pt2=randint(pt2,len(p1)-2)
        child1=p1[:pt1]+p2[pt1+1:pt2]+p1[pt2+1:]
        child1=p2[:pt1]+p1[pt1+1:pt2]+p2[pt2+1:]
    return [child1,child2]
        
# mutation
def mutation(bitstring, r_mut):
    for i in range(len(bitstring)):
        # check for a mutation
        if rand() < r_mut:
            # flip the bit
            bitstring[i] = 1 - bitstring[i]

# genetic algorithm
def genetic_algorithm(objective, n_bits, n_iter, n_pop, r_cross, r_mut):
    # initial population of random bitstring
    pop = [randint(0, 2, n_bits).tolist() for _ in range(n_pop)]
    
    best, best_eval = pop[0], objective(pop[0])
    # enumerate generations
    for gen in range(n_iter):
        # evaluate all candidates in the population
        scores = [objective(c) for c in pop]
        # for score in scores:
        #     print('score: ',score)
        # check for new best solution
        for i in range(n_pop):
            if scores[i] < best_eval:
                best, best_eval = pop[i], scores[i]
                # if best_eval==0:
                #     print('Found bent function: ',best)
                # print(">%d, new best f(%s) = %f" % (gen,  pop[i], scores[i]))
                current_non_lin=mx_non_linearity-best_eval
                if(current_non_lin>=THRESH_HOLD*mx_non_linearity):
                    return [best,best_eval]
        # select parents
        selected = [selection(pop, scores) for _ in range(n_pop)]
        # create the next generation
        children = list()
        for i in range(0, n_pop, 2):
            # get selected parents in pairs
            p1, p2 = selected[i], selected[i+1]
            # crossover and mutation
            for c in crossover(p1, p2, r_cross):
                # mutation
                mutation(c, r_mut)
                # store for next generation
                children.append(c)
        # replace population
        pop = children
    return [best, best_eval]
for i in range(8,17,2):
    start_time=time.time()
    # define the total iterations
    n_iter = 200
    # variables
    var = i
    # bits
    n_bits = 2**var
    # define the population size
    n_pop = 200
    # crossover rate
    # r_cross = 0.6
    r_cross=2/var
    # mutation rate
    r_mut = 0.8
    # r_mut=0.6
    # perform the genetic algorithm search
    mx_non_linearity = 2**(var-1)-2**(var/2-1)
    # print('max possible score is : ', 2**(var-1)-2**(var/2-1))
    best, score = genetic_algorithm(getScore, n_bits, n_iter, n_pop, r_cross, r_mut)
    filename="myResults_"+str(var)+".txt"
    file1 = open(filename, 'w')

    print('Execution completed!')
    print('max possible nonlinearity is : ', mx_non_linearity)
    print('max nonlinearity obtained: ',mx_non_linearity-score)
    print('In terms of percentage: ',100*(mx_non_linearity-score)/mx_non_linearity)
    ones,zeroes=0,0
    for i in best:
        if i==0:
            zeroes+=1
        else:
            ones+=1
    print('ones: ',ones,' zeroes: ',zeroes)
    print('time taken: ',time.time()-start_time, 'seconds ')
    file1.write('\nmax possible nonlinearity is : {}'.format( mx_non_linearity))
    file1.write('\nmax nonlinearity obtained: {}'.format( mx_non_linearity-score))
    file1.write('\nIn terms of percentage: {}'.format( 100*(mx_non_linearity-score)/mx_non_linearity))
    file1.write('\ntime taken: {}'.format( time.time()-start_time))
    file1.write('function: {}'.format(best))




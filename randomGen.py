from numpy.random import rand
from numpy.random import randint
from sympy import fwht
import time


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

my_dict = dict()

def getScore(seq):
    
    tup_seq = tuple(seq)
    if tup_seq in my_dict:
        return my_dict[tup_seq]
    use_seq = [i for i in seq]
    convert_to_polarised(use_seq)
    transform = fwht(use_seq)
    mx = max(abs(min(transform)), max(transform))
    curr_non_linearity = 2**(var-1)-mx/2
    my_dict[tup_seq] = mx_non_linearity-curr_non_linearity
    return mx_non_linearity-curr_non_linearity


# making a program to randomly generate boolean functions with high nonlinearity
for i in range(8, 17, 2):
    start_time = time.time()
    var = i
    # bits
    n_bits = 2**var
    mx_non_linearity = 2**(var-1)-2**(var/2-1)

    fn = randint(0, 2, n_bits).tolist()
    score=getScore(fn)
    best=fn
    for h in range(0,4000):
        fn = randint(0, 2, n_bits).tolist()
        if(getScore(fn)<score):
            score=getScore(fn)
            best=fn
        

    filename = "myRandomResults_"+str(var)+".txt"
    file1 = open(filename, 'w')

    print('Execution completed!')
    print('max possible nonlinearity is : ', mx_non_linearity)
    print('max nonlinearity obtained: ', mx_non_linearity-score)
    print('In terms of percentage: ', 100 *
          (mx_non_linearity-score)/mx_non_linearity)
    ones, zeroes = 0, 0
    for i in best:
        if i == 0:
            zeroes += 1
        else:
            ones += 1
    print('ones: ', ones, ' zeroes: ', zeroes)
    print('time taken: ', time.time()-start_time, 'seconds ')
    file1.write('\nmax possible nonlinearity is : {}'.format(mx_non_linearity))
    file1.write('\nmax nonlinearity obtained: {}'.format(
        mx_non_linearity-score))
    file1.write('\nIn terms of percentage: {}'.format(
        100*(mx_non_linearity-score)/mx_non_linearity))
    file1.write('\ntime taken: {}'.format(time.time()-start_time))
    file1.write('function: {}'.format(best))



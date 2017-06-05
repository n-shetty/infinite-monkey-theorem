from __future__ import print_function
import numpy as np
from string import join
import time
from joblib import Parallel, delayed
import multiprocessing
import sys

target_string = "scooby"# dooby doo"
epochs = int(1e8) # maximum number of iterations to run
num_cores = multiprocessing.cpu_count()

print("Length of the target string: ***'{}'*** is {}".format(target_string, len(target_string)))
print("Using {} cores on this machine".format(num_cores))

# generate a set of alphabets and a space
unique_text = "quick brown fox jumps over the lazy dog"
unique_letter = {letter for word in unique_text for letter in word}
print("Following are the alphabets, including space: ")
print(*unique_letter)

"""
# a function that generates random text given a character length
def gen_rand_text(char_len):
    return join(np.random.choice(list(unique_letter),char_len), "")

program_starts = time.time()

for index in range(10000000):
    now = time.time()
    if target_string == gen_rand_text(len(target_string)):
        print("Target string generated in {}".format(index))
        break
       
print("It has been {0} seconds since the loop started".format(now - program_starts))       
"""

# a function that generates random text given a character length, and compares with target string
def gen_rand_text():
    np.random.seed() # use different seeds on different cores
    rand_string = join(np.random.choice(list(unique_letter),len(target_string)), "")
    if target_string == rand_string:
        print("Random string generated is equivalent to the target string: {}".format(rand_string))
        print("If the target string is not generated, try again or increase the number of epochs")
        exit()
       
# generate random text on multiple cores (parallelization)
inputs = range(epochs)
_ = Parallel(n_jobs=num_cores)(delayed(gen_rand_text)() for i in inputs)
print("If the target string is not generated, try again or increase the number of epochs")

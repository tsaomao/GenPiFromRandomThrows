# Process per group of trials:
#   Process per trial:
#     Process per observation:
#       Generate 2 numbers
#       Test for coprimality
#     Count number of coprimes in a field of some number of pairs
#     Find observed probability of these coprimes
#     Calculate pi from sqrt(6/observed probability)
#   Compare pi from each trial to true value
# Figure out where/whether to/how to dump raw data and/or trial results meta
#  data to external data dump

import math
import random

def evalRandomPair():
	random.seed()
	r1 = random.randrange(randomrange)
	r2 = random.randrange(randomrange)
	if math.gcd(r1, r2) > 1:
		return 1
	else:
		return 0

# Check arguments for override option
# Check second for parameters file and read parameters from that
# If no override options or parameters file, prompt for parameters
# Default parameters:
# trialsize defines number of random pairs
trialsize = 1000
# randomrange defines upper value of random range
randomrange = 500


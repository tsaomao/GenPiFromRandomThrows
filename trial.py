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


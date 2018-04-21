import random

CS_VALID = 1
CS_DIRTY = 2

class Cache: 

    # constructor 
    # 2**n : total number of bytes in cache
    # 2**b : block size
    # 2**a : set associativity
    def __init__(self, n, b, a):
        self.verbose = 0 
        self.nb_n = n
        self.nb_b = b
        self.nb_a = a

        # set other variables you may need
        # TODO

        self.set_replacement_policy(1) # LRU
        self.reset()

    def reset(self):
        # we do not care about data
        # create list (or arrays) for tags, flags, set_flags
        # TODO
        self.num_references = 0
        self.num_misses = 0

    def set_verbose(self, v):
        self.verbose = v

    # policy 
    #   0:  random
    #   1:  LRU
    def set_replacement_policy (self, v):
        self.replacement = v

    # find a block in a set where the new block can be placed
    def find_way(self, index):
        if (self.associativity == 1):
            # print("finding way, returning 0")
            return 0

        way = 0
        # check if there is a way available
        # if yes, return the way number
        # if not, find a block by replacement policy
        # TODO
        return way 

    # bookkeeping. Just accessed block identified by index and way
    def update_set_flags(self, index, way):
        if self.associativity <= 1:
            return
        # if using LRU, maitain the access history for replacement
        # TODO

    # do not care about write for now
    # return 1 for hit
    # return 0 for miss
    def access(self, addr, write):
        self.num_references += 1
        hit = 0
        way = 0
        index = 0

        # cache access. ignore write for now.
        # steps: 
        #   obtain index and tag
        #   check if it is a hit
        #   if it is a miss, replace a block in the set
        # TODO
        self.update_set_flags(index, way)
        return hit

    # report the statistics
    def report(self):
        print("Number of references = {}".format(self.num_references))
        print("Number of misses     = {}".format(self.num_misses))
        print("Number of hits       = {}".format(self.num_references - self.num_misses))
        if (self.num_references):
            print("Miss rate            = {:.2f}%".format(self.num_misses * 100.0 / self.num_references))


from random import randint


class Node:
    def __init__(self,node_id,delay):
        self.node_id = node_id
        self.delay = delay
        self.preprocessing_phase = randint(1,5)
        self.discretization_phase = randint(1,5)
        self.att_reduct_phase = randint(1,5)
        self.train_test_phase = randint(1,5)

    def print_node(self):
        print "\n\tNode ID: " + str(self.node_id + 1)
        print "\tDelay: " + str(self.delay)
        print "\tTime taken for Data mining Processes\n\tPreprocessing Phase: " + str(self.preprocessing_phase)
        print "\tDiscretization Phase: " + str(self.discretization_phase)
        print "\tAttribute reduction Phase: " + str(self.att_reduct_phase)
        print "\tTraining & Testing Phase: " + str(self.train_test_phase)


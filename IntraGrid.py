import Node
from random import randint


def find_min(a,b,c):
    minval = min(a,b,c)
    if minval == a:
        return 0
    elif minval == b:
        return 1
    return 2


# This class represents the grid of system
class Intragrid:

    #Methods for grid goes here
    def __init__(self, grid_id, number_of_nodes):
        self.grid_id = grid_id;
        self.number_of_nodes = number_of_nodes
        self.node_list = [Node.Node(count,randint(1,5)) for count in range(number_of_nodes)]
        self.response_time = randint(5,10)
        self.active = True
        return

    def print_grid(self):
        print "\nGrid ID: "+ str(self.grid_id + 1)
        print "\nNumber of Nodes: " + str(self.number_of_nodes)
        print "\nThe nodes in system are as follow:"
        for i in range(int(self.number_of_nodes)):
            Node.Node.print_node(self.node_list[i])

    def predict_survival(self, job, age, sex):
        import subprocess
        grid_no = int(self.grid_id) +1
        result = subprocess.check_output(["Rscript", "/home/dipti/Desktop/ddminer_data_mining.R", str(grid_no), str(age), str(sex)])
        print result
        if(job == 1):
            self.job_migration()
        else:
            self.without_job_migration()
        return result

    def deactivate(self):
        self.active = False
        return

    def activeness(self):
        if (self.active):
            return True
        return False

    def job_migration(self):
        print "JOB Migration in Process..."
        for i in range(4):
            if i==1:
                stage= 'Preprocessing Phase'
                machine_index = find_min(self.node_list[0].preprocessing_phase, self.node_list[1].preprocessing_phase,self.node_list[2].preprocessing_phase)
                print "\nFor " + str(stage) + " the external scheduler will select machine :" + str(machine_index)
            elif i==2:
                stage= 'Discretization Phase'
                machine_index = find_min(self.node_list[0].discretization_phase, self.node_list[1].discretization_phase,self.node_list[2].discretization_phase)
                print "\nFor " + str(stage) + " the external scheduler will select machine :" + str(machine_index)
            elif i==3:
                stage= 'Attribute reduction Phase'
                machine_index = find_min(self.node_list[0].att_reduct_phase, self.node_list[1].att_reduct_phase,self.node_list[2].att_reduct_phase)
                print "\nFor " + str(stage) + " the external scheduler will select machine :" + str(machine_index)
            elif i==4:
                stage= 'Training & Testing Phase'
                machine_index = find_min(self.node_list[0].train_test_phase, self.node_list[1].train_test_phase,self.node_list[2].train_test_phase)
                print "\nFor " + str(stage) + " the external scheduler will select machine :" + str(machine_index)

    def without_job_migration(self):
        print "Without JOB Migration..."
        machine_index = find_min(self.node_list[0].preprocessing_phase, self.node_list[1].preprocessing_phase,self.node_list[2].preprocessing_phase)
        print "\nThe external scheduler will select machine :" + str(machine_index)+ " for all:"
        print "\tPreprocessing Phase "
        print "\tDiscretization Phase "
        print "\tAttribute reduction Phase "

    def internal_scheduling(self):
        while True:
            op= input("\nEnter your choice\n1. With job migration\n2. Without job migration\n")
            if(op==1):
                self.job_migration()
                break
            elif(op==2):
                self.without_job_migration()
                break
            else:
                print "Enter valid option."

    def compute_response_time(self):
        return self.response_time


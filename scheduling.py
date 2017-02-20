import IntraGrid
import json
from pprint import pprint
internal_scheduling_mode = 0
node_list = []


def find_min(a,b,c):
    minval = min(a,b,c)
    if minval == a:
        return 0
    elif minval == b:
        print '1'
        return 1
    print '2'
    return 2


def create_grids(no_of_grids):
    print no_of_grids
    grid_list = [IntraGrid.Intragrid(count, 3) for count in range(int(no_of_grids))]
    return grid_list


def view_network(no_of_grids,grid_list):
    for i in range(int(no_of_grids)):
        IntraGrid.Intragrid.print_grid(grid_list[i])


def external_scheduling(no_of_grids, grid_list,age,sex):
    flag = 0
    '''for i in range(int(no_of_grids)):
        index = find_min(grid_list[0].response_time,grid_list[1].response_time,grid_list[2].response_time)
        print index
    IntraGrid.Intragrid.deactivate(grid_list[index])'''
    result_list = []
    for i in range(int(no_of_grids)):
        print i
        if IntraGrid.Intragrid.activeness(grid_list[i]):
            result_list.append(IntraGrid.Intragrid.predict_survival(grid_list[i],internal_scheduling_mode,age,sex))
    return result_list


def global_synthesis(result_list):
    yes_count = result_list.count('YES')
    no_count = result_list.count('NO')
    print 'In GS'
    if yes_count>no_count:
        return 'YES'
    return 'NO'


def read_json():
    with open('Inputdata.json') as data_file:
        data = json.load(data_file)
    pprint(data)
    no_of_grids = data[u'no_of_grids']
    no_of_nodes = data['no_of_nodes']
    internal_scheduling_mode = data[u'Internal_Scheduling_mode']
    print "no_of_grids = " + no_of_grids + " no_of_nodes: " + no_of_nodes
    return no_of_grids


def predict(age,sex):
    no_of_grids = read_json()
    locallist = create_grids(no_of_grids)
    view_network(no_of_grids,locallist)
    result= external_scheduling(no_of_grids,locallist, age, sex)
    survival = []
    final_prediction = global_synthesis(result)
    survival.append(final_prediction)
    survival = execution(survival,locallist,no_of_grids)
    print survival
    return survival


def execution(survival,grid_list,no_of_grids):
    for i in range(int(no_of_grids)):
        survival.append(IntraGrid.Intragrid.compute_response_time(grid_list[i]))
    return survival

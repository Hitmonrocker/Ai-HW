import random
import queue
''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''
'''
                For Search Algorithms 
'''
''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''

'''
BFS add to queue 
'''
def add_to_queue_BFS(node_id, parent_node_id, cost, initialize=False):
    # Your code here
     return

'''
BFS add to queue 
'''
def is_queue_empty_BFS():
    # Your code here
    return False

'''
BFS pop from queue
'''
def pop_front_BFS():
    (node_id, parent_node_id) = (0, 0)
    # Your code here
    return (node_id, parent_node_id)

'''
DFS add to queue 
'''
def add_to_queue_DFS(node_id, parent_node_id, cost, initialize=False):
    # Your code here
    return

'''
DFS add to queue 
'''
def is_queue_empty_DFS():
    # Your code here
    return False

'''
DFS pop from queue
'''
def pop_front_DFS():
    (node_id, parent_node_id) = (0, 0)
    # Your code here
    return (node_id, parent_node_id)

'''
UC add to queue 
'''
def add_to_queue_UC(node_id, parent_node_id, cost, initialize=False):
    # Your code here
    return

'''
UC add to queue 
'''
def is_queue_empty_UC():
    # Your code here
    return False

'''
UC pop from queue
'''
def pop_front_UC():
    (node_id, parent_node_id) = (0, 0)
    # Your code here
    return (node_id, parent_node_id)

'''
A* add to queue 
'''
def add_to_queue_ASTAR(node_id, parent_node_id, cost, initialize=False):
    # Your code here
    return

'''
A* add to queue 
'''
def is_queue_empty_ASTAR():
    # Your code here
    return False

'''
A* pop from queue
'''
def pop_front_ASTAR():
    (node_id, parent_node_id) = (0, 0)
    # Your code here
    return (node_id, parent_node_id)

''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''
'''
                For n-queens problem 
'''
''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''


'''
Compute a random state 
'''
def get_random_state(n):
    state = []
    random.seed();
    for x in range(0,n):
    	state[x] = random.randint(0,7);
    return state

'''
Compute pairs of queens in conflict 
'''
def compute_attacking_pairs(state):
    number_attacking_pairs = 0
    for x in xrange(0,len(state)):
    	col_curr = state[x]
    	for y in xrange(x,len(state)):
    		col_comp = state[y]
    		if(col_curr==col_comp):
    			number_attacking_pairs+=1
    		if(col_curr==col_comp+x):
    			number_attacking_pairs+=1
    		if(col_curr==col_comp-x):
    			number_attacking_pairs+=1
    return number_attacking_pairs

'''
The basic hill-climing algorithm for n queens
'''
def hill_desending_n_queens(state, comp_att_pairs):
    final_state = []
    new_state = state;
    num_atk = 0;
    while(new_state != final_state):
    	
    	num_atk = comp_att_pairs(new_state)

		if(num_atk == 0)
    		return final_state;

		for x in xrange(len(state),0,-1):
			if(comp_att_pairs(state[x]+1)<num_atk && (state[x]+1)<7):
				state[x]+=1;
	    	if(comp_att_pairs(state[x]-1)<num_atk && (state[x]-1)>0):
	    		state[x]-=1;
	    final_state = new_state;
	    new_state = state;
    return final_state

'''
Hill-climing algorithm for n queens with restart
'''
def n_queens(n, get_rand_st, comp_att_pairs, hill_descending):
    final_state = []
    old_state = get_rand_st(n);
    final_state = old_state;
   	while(comp_att_pairs(final_state)!=0):
   		old_state = final_state;
   		final_state = hill_descending(start_state,comp_att_pairs);
   		if((final_state == old_state).all()):
   			final_state = get_rand_st(n);
    return final_state







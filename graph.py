def krushkals(adj_list):
    '''Return a minimum spanning tree of adj_list using Krushka's algo.'''

    adj_list = dict(adj_list)
    expected_mst_edges = (len(adj_list.keys()) - 1) * 2
    mst = {k:[] for k in adj_list}
    for node in adj_list:
        adj_list[node].sort(key=lambda x: x[1]) # Sort by weight edge
        
    while get_edge_num(mst) < expected_mst_edges:
        min_edge = get_min_weight_edge(adj_list)
        first_node = min_edge[0]
        sec_node = min_edge[1]
        weight = min_edge[2]
        
        if not does_create_cycle(mst, min_edge): # Then include edge in MST
            edge_first_node = (sec_node, weight)
            edge_sec_node = (first_node, weight)
            mst[first_node].append(edge_first_node)
            mst[sec_node].append(edge_sec_node)
        
        del adj_list[first_node][0]
        del adj_list[sec_node][0]        
    return mst

def get_min_weight_edge(adj_list):
    '''Return the edge with minimum weight in adj_list.'''

    min_edge = None
    for key in adj_list:
        if adj_list[key]: # If this node has edges
            cur_edge= [key] + list(adj_list[key][0])
            if min_edge is None:
                min_edge = [key] + list(cur_edge)
        min_edge = min(min_edge, cur_edge, key= lambda x: x[2])    
    return min_edge

def does_create_cycle(adj_list, edge):
    '''Return whether edge creates a cycle in adj_list.'''

    return is_connected(adj_list, edge[0]) and is_connected(adj_list, edge[1])
    
def is_connected(adj_list, node):
    ''' Return whether there is an edge in adj_list connected to node.'''

    for key in adj_list:
        if node in adj_list[key]:
            return True
    return False
        
def get_edge_num(adj_list):
    ''' Return the total number of edges in the graph (adj_list.'''

    return sum([len(v) for k,v in adj_list.iteritems()])
    
#def prim(adj_list):
    #'''Return a minimum spanning tree of adj_list using Prim's algo.'''

    #adj_list = dict(adj_list)
    #expected_mst_edges = (len(adj_list.keys()) - 1) * 2
    #mst = {k:[] for k in adj_list}
    #for node in adj_list:
        #adj_list[node].sort(key=lambda x: x[1])
    
    
    
if __name__ == "__main__":
    adj_list = {}
    adj_list['a'] = [('c', 90), ('d', 3000), ('e', 2000), ('b', 60)]
    adj_list['b'] = [('a', 60), ('c', 6000), ('d', 4000), ('e', 50)]
    adj_list['c'] = [('a', 90), ('d', 80), ('b', 6000)]
    adj_list['d'] = [('c', 80), ('a', 3000), ('b', 4000), ('e', 70)]
    adj_list['e'] = [('b', 50), ('d', 70), ('a', 2000)]
    a =  krushkals(adj_list)
    print a
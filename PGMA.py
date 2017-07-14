# Метрика,эпигенетика,оптогенетика, WPGMA, UPGMA, neighbour joining
def hamming_distance(line_1, line_2):
    counter = 0
    for i in range(len(line_1)):
            if line_1[i] != line_2[i]:
                counter += 1
    return counter

def get_distance(file_name):
    seq = {}
    distance = {}
    with open(file_name) as f:
        for line in f:
            name, sequence = line.strip().split('  ')
            seq[name] = sequence
        for name_1 in seq:
            for name_2 in seq:
                if name_1 == name_2:
                     continue
                if name_1 not in distance:
                     distance[name_1] = {}
                if name_2 not in distance:
                    distance[name_2] = {}
                    distance[name_1][name_2] = hamming_distance(seq[name_1], seq[name_2])
                    distance[name_2][name_1] = hamming_distance(seq[name_1], seq[name_2])
    return distance                
            
def PGMA(D, tree):

    if len(D) == 0:
        return tree
    
    minimum = 100000
    min_pair =['', '']
    for symbol_1 in D:
        for symbol_2 in D[symbol_1]:
            if D[symbol_1][symbol_2] < minimum:
                minimum = D[symbol_1][symbol_2]
                min_pair[1] = symbol_1
                min_pair[0] = symbol_2
                new_symbol = min_pair[1] + min_pair[0]
                
    print('Min pair: {min_pair}'.format(min_pair=min_pair))
    new_distance = 0
 # min_pair = [M, N]
    for key in D[min_pair[0]]:
    # key = {L: 5, K: 5}
        if key in min_pair:
            continue
        
        new_distance = (D[min_pair[0]][key] + D[min_pair[1]][key]) / 2
        if ''.join(min_pair) in D:
            D[''.join(min_pair)][key] = new_distance
        else:
            D[''.join(min_pair)] = {key: new_distance}
        print(D)
        D[key][''.join(min_pair)] = new_distance

    prev_value_1 = 1
    prev_value_2 = 1
    if min_pair[0] in tree:
        prev_value_1 = tree[min_pair[0]]
        del tree[min_pair[0]]
    if min_pair[1] in tree:
        prev_value_2 = tree[min_pair[1]]
        del tree[min_pair[1]]
        
    tree[''.join(min_pair)] = {min_pair[0]: prev_value_1}
    tree[''.join(min_pair)][min_pair[1]] = prev_value_2
    
    del D[min_pair[0]]
    del D[min_pair[1]]
    for key in D:
        if key == ''.join(min_pair):
            continue
        print(key)
        del D[key][min_pair[0]]
        del D[key][min_pair[1]]
    print(D)                   
    return PGMA(D, tree)
            
print(get_distance('UNPHASEDconcateneted'))     
                    

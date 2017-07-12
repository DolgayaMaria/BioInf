def add_out_kmers(out,kmers,k):
    for i in range(len(kmers)-1): 
        prekmer = kmers[i]
        postkmer = kmers[i+1]
        if prekmer not in out: 
            out[prekmer] = {}
        if postkmer not in out[prekmer]:
            out[prekmer][postkmer] = [0, prekmer + postkmer[k-1:]]
        out[prekmer][postkmer][0] += 1
    return out

def add_in_kmers(in_,kmers,k):
    for i in range(len(kmers)-1): 
        prekmer = kmers[i]
        postkmer = kmers[i+1]
        if postkmer not in in_:
            in_[postkmer] = {}
        if prekmer not in in_[postkmer]:
            in_[postkmer][prekmer] = [0, prekmer + postkmer[k-1:]]
        in_[postkmer][prekmer][0] += 1
    return in_

def condense(out, in_, k):
    for v in list(out.keys()):
        new_cov = 0.0
        new_len = ''
        left_len = ''
        left_cov = ''
        right_len = ''
        right_cov = ''
        res_string = ''
        
        if v not in in_:
            continue
        
        if len(out[v]) != 1 or len(in_[v]) != 1:
            continue
        
        prev = list(in_[v].keys())[0]
        nex = list(out[v].keys())[0]
        left_seq = out[prev][v][1]
        right_seq = out[v][nex][1]
        left_cov = out[prev][v][0]
        right_cov = out[v][nex][0]
        
        new_seq = left_seq + right_seq[k:]
        new_cov = (len(left_seq)*left_cov + len(right_seq)*right_cov)/len(new_seq)
        out[prev][nex] = [new_cov, new_seq]
        in_[nex][prev] = [new_cov, new_seq]

        del out[prev][v]
        del in_[nex][v]
        del out[v]
        del in_[v]
            
    return out, in_

def get_aver(graph_out):
    total_cov = 0.0
    total_len = 0.0
    total_edge_number = 0
    for smth in graph_out:
        graph_out_1 = graph_out[smth]
        for smth1 in graph_out_1:
            smth1 = graph_out_1[smth1]
            print(smth1)
            total_cov += smth1[0]
            total_len += len(smth1)
            total_edge_number += 1
    aver_cov = total_cov/total_edge_number
    aver_len = total_len/total_edge_number

    return aver_cov, aver_len



def remove_tips(graph_in, graph_out):
    avg_cov = 0.0
    avg_len = 0.0
    nb_edges = 0

    for left in graph_out:
        for right in graph_out[left]:
            edge = graph_out[left][right]
            avg_cov += edge[0]
            avg_len += len(edge[1])
            nb_edges += 1
    avg_cov /= nb_edges
    avg_len /= nb_edges

    deleted = False

    graph_in_keys = list(graph_in.keys())

    for key in graph_in_keys:
        graph_in_1 = graph_in[key]
        if key in graph_out:
            continue

        if len(graph_in[key]) > 1:
            continue

        parent_key = list(graph_in[key].keys())[0]
        edge = graph_in[key][parent_key]

        if edge[0] < avg_cov / 3 and len(edge[1]) < avg_len / 3:
            del graph_out[parent_key][key]
            del graph_in[key]
            deleted = True

    return deleted

def extract_kmers(read, k):
    res = []
    for i in range(0,len(read)-k+1):
        res.append(read[i:i+k])
               
    return res


def fastq(file_name):
    with open (file_name) as f:
        counter = 0
        rid = []
        for line in f:
            line = line.strip()
            if counter % 4 == 1:
                rid.append(line)
            counter += 1
    return rid


def create_de_bruijn_graph_from_fastq(file_name,k):
    graph_in = {}
    graph_out = {}
    rids = fastq(file_name)
    for rid in rids:
        kmers = extract_kmers(rid, k)
        graph_in = add_in_kmers(graph_in,kmers,k)
        graph_out = add_out_kmers(graph_out,kmers,k)
    condense(graph_out, graph_in, k)
    while remove_tips(graph_in, graph_out):
        condense(graph_out, graph_in, k)
    return graph_in, graph_out

graph_in, graph_out  = create_de_bruijn_graph_from_fastq('/Users/Guest/Documents/BioInf/BioInf/s_6.first1000.fastq', 14)

print(graph_in, graph_out)

def dump_graph(outgoing, viz_fname):
    with open(viz_fname, 'w') as out_f:
        print('digraph ag{', file=out_f)
        for left, dict in outgoing.items():
            for right in dict:
                round_coverage = dict[right][0]
                print(left + '[label="{}"]'.format(left), file=out_f)
                print(right + '[label="{}"]'.format(right), file=out_f)
                print(
                    left + ' -> ' + right +
                    '[label="C = {}"]'.format(round_coverage),
                    file=out_f)
        print('}', file=out_f)


dump_graph(graph_out,'/Users/Guest/Documents/BioInf/BioInf/file_for_graph.txt')

        

with open ('/Users/Guest/Documents/gene_counts/genome_annotation.gtf') as f:
    a = []
    for line in f:
        gene_info = line.strip().split('\t')
        gene_coordinate1 = gene_info[3]
        gene_coordinate2 = gene_info[4]
        strand = gene_info[6]
        gene_name = gene_info[8].split('; ')[2].strip('gene_name').strip('"')
        a.append([int(gene_coordinate1), int(gene_coordinate2), strand, gene_name])

gene_count = {}
for gene in a:
    gene_count[gene[3]] = 0

with open('/Users/Guest/Documents/gene_counts/TNOR2_22.sam') as f:
    first_gene_i = 0
    for line in f:
        read_info = line.strip().split('\t')
        if line[0] == '@':
            continue
        read_flag = read_info[1]
        read_coordinate = read_info[3]
        read_lenth = len(read_info[9])
        
        g_c1 = int(gene_coordinate1)
        g_c2 = int(gene_coordinate2)
        r_c1 = int(read_coordinate) # ivan.dmitrievsky@gmail.com
        r_c2 = r_c1 + read_lenth

        while first_gene_i < len(a):
            gene = a[first_gene_i]
            if r_c2 < gene[0]:
                break
            if (gene[0] < r_c1 < gene[1] ) or (gene[0] < r_c2 < gene[1]):
                gene_count[gene[3]] += 1
                break
            if r_c1 > gene[1]:
                first_gene_i += 1
                
          


                
                
                
                
                
                
                
                
                
            
            

    

        

    
    
        
        

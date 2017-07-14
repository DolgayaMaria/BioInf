import math
import matplotlib.pyplot as my_super_module
# Подсчет ридов выровненных на гены - оценка экспрессии генов (экспрессия)
# Дифференциальная экспрессия - сравнение эспрессии генов больных и здоровых людей

with open ('/home/aleksandrsl/Projects/gotocamp/diff_expr/norm_camp.tsv') as f:
    line = f.readline().strip().split('\t')
    control_quantify = []
    case_quantify = []
    for i in range(len(line)):
        if line[i] == 'control':
            control_quantify.append(i)
        elif line[i] == 'case':
            case_quantify.append(i)
    average_total = []
    diff = []
    gene_names = []
    for line in f:

        gene = line.strip().split('\t')
        gene_names.append(gene[0])
        control_num = 0
        case_num = 0
        total_num = 0
        for i in range (control_quantify[0], control_quantify[-1] + 1):
            control_num += float(gene[i])
        aver_control = control_num/len(control_quantify)

        for i in range (case_quantify[0], len(gene)):
            case_num += float(gene[i])
        aver_case = case_num/len(case_quantify)
        
        for i in range(control_quantify[0],len(gene)):
            total_num += float(gene[i])
        average_total.append( total_num/(len(control_quantify)+len(case_quantify)))
        diff.append(math.log2(aver_case/aver_control))
        print(diff)

my_super_module.plot(average_total,diff, 'ro')
my_super_module.show()

target_gene = []
for i in range(len(diff)):
    if abs(diff[i]) > 0.1:
         target_gene.append(i)

gene_list = []
for i in target_gene:
    gene_list.append(gene_names[i])

with open ('Diff_Expression.tsv','w') as file:

    file.write('gene_symbol\tlog_fc\n')
    for i in range (len(gene_list)):
        file.write('{}\t{}\n'.format(gene_list[i], diff[i]))








            
            
    
            

        
    

def fastq(file_name):
    with open (file_name) as f:
        counter = 0
        rid = []
        for line in f:
            line = line.strip()
            if counter % 4 == 0:
                rid.append(line)
                continue
            if counter % 4 == 1:
                rid.append(line)
                continue
            if counter % 4 == 2:
                continue
            if counter % 4 == 3:
                rid.append(line)
            counter += 1

    return rid

fastq('/Users/Guest/Documents/BioInf/BioInf/test.fastq')
    
    

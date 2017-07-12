def F(string):
    counter = 0
    res_1 = ''
    res = {string[i]:counter for i in range(len(string))}
      
    for i in range(len(string)):
        if string[i] in res:
            res[string[i]] += 1

    for item in res.items():
        res_1 += item[0]
        res_1 += ' '
        res_1 += str(item[1])
        res_1 += ', '
        

    return res_1[:-2]

        

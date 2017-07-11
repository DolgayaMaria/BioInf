def F(list_1, list_2):
    
    res_list = []
    for i in range(0, len(list_1)):
        for j in range(0, len(list_2)):
            if list_1[i] == list_2[j] and list_1[i] not in res_list:
                res_list.append(list_1[i])
            
            
            
    return res_list

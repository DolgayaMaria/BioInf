def F(file_name):
    with open (file_name) as f:
        res = []
        for values in f:
            res.append(values)
            res = res[::-1]

        return res
        

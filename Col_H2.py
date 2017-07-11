def F(text):
    text = text.split()
    text.sort()
    res = ''
    counter = 1
    maximum = 0
    for word in range(len(text)):
        if text[word] == text[word-1]:
            counter += 1
        else:
            if maximum < counter:
                maximum = counter
                res = text[word-1]
            counter = 1
    return res
       
        
        
        
        

def F(t):
    text = t.split(',').srtip('/t')
    counter = {}
    for word in text:
        if text[word] == text[word + 1]:
            counter[word] += 1
        else:
        m = max(counter[word])
        
        
        
        

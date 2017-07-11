def F(string):
    string = list(string)
    alph = 'abcdefghijklmnopqrstuvwxyz'
    vow = 'aeiouy'
    postvow = 'bfjpvz'

    for letter in range(len(string)):
        if string[letter] in vow:
            string[letter] = postvow[vow.find(string[letter])]
        elif string[letter] in alph:
            string[letter] = alph.find(string[letter])

    return string

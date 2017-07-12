import math


def F(len1, len2, len3):
    p = (len1 + len2 + len3)/2
    S = math.sqrt((p - len1)*(p - len2)*(p - len3))
    
    S = S*p
    return S

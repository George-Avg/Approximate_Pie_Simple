def num_format(x):
    x = str(x)
    zeros = str(x.count('0'))
    x = x.replace('0','')
    return x + " *10^" + zeros

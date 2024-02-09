from decimal import Decimal, getcontext
from pie import pi, accuracy
from num_format import num_format

getcontext().prec = accuracy

prev_dif = float('inf')
for n in range(1, 2000):
    x = Decimal(round(pi ** n))
    dif = abs(x ** (Decimal(1 / n)) - pi)
    if dif < prev_dif:
        print('!!!BEST MUCH!!!')
        best_n = n
        best_x = x
        best_dif = dif

    prev_dif = dif
    # dif = "{:.4e}".format(dif)
    print(f'n = {n}'
          f'\nx = {num_format(x)}'
          f'\naccuracy = {dif:.4e}'
          f'\n __________________________________________________________________')

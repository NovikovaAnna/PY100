# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint

tmp = []
for n in range(16):
    tmp.append({'bin': bin(n), 'dec': n, 'hex': hex(n), 'oct': oct(n)})
pprint(tmp)
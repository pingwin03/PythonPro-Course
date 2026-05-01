# Iloczyn elementów: Użyj funkcji reduce() , aby obliczyć iloczyn (wynik mnożenia)
# wszystkich liczb w liście [1, 2, 3, 4, 5] .

from functools import reduce
from operator import mul

liczby = [1, 2, 3, 4, 5]
iloczyn = reduce(mul, liczby)

print(iloczyn)

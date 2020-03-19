
from __future__ import division
import math
while True:





    def primenumbers(x):
        while x % 2 == 0:
            print(2)
            x = x / 2

        for i in range(3, int(math.sqrt(x)) + 1, 2):
            while x % i == 0:
                print(i)
                x = x / i

        if x > 2:
            print(int(x))


    x1 = int(input("skriv talet du vill faktorisera :"))

    primenumbers(x1)

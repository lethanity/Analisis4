import math
from decimal import Decimal


class Tp1:


    def mathpi(self):
        return math.pi


    def gauss_legendre_float(self, n):
        a = 1.0
        b = 1.0/math.sqrt(2)
        t = 1/4.0
        p = 1.0

        for i in range(n):
            x = (a+b)/2
            y = math.sqrt(a*b)
            t = t - p*math.pow((a - x),2)
            a = x
            b = y
            p = 2.0*p

        return math.pow((a + b),2)/(4.0*t)


    def gauss_legendre_decimal(self, n):
        a = Decimal(1)
        b = Decimal(1)/Decimal(math.sqrt(2))
        t = Decimal(1/4.0)
        p = Decimal(1)

        for i in range(n):
            x = Decimal((a+b)/2)
            y = Decimal(math.sqrt(a*b))
            t = Decimal(t - p* Decimal(math.pow((a - x),2)))
            a = Decimal(x)
            b = Decimal(y)
            p = Decimal(2*p)

        return Decimal(Decimal(math.pow((a + b),2))/(Decimal(4)*t))

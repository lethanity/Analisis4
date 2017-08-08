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

    def pi_digits(self, n):
        k, a, b, a1, b1 = 2, 4, 1, 12, 4
        while n > 0:
            p, q, k = k * k, 2 * k + 1, k + 1
            a, b, a1, b1 = a1, b1, p * a + q * a1, p * b + q * b1
            d, d1 = a / b, a1 / b1
            while d == d1 and n > 0:
                yield int(d)
                n -= 1
                a, a1 = 10 * (a % b), 10 * (a1 % b1)
                d, d1 = a / b, a1 / b1

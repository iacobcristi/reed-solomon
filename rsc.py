import string

class ReedSolomon:

    def __init__(self, k, s, p, m):
        self.k = k
        self.s = s
        self.p = p
        self.m = m
        self.n = k + 2 * s

    def poly(self, a_list, x):
            ans = 0
            p = self.k - 1
            for a in a_list:
                ans += (a*x**p) % 11
                p = p - 1
            return ans % 11

    def int2base(self, x, base):
        digs = string.digits + string.ascii_letters
        if x < 0:
            sign = -1
        elif x == 0:
            return digs[0]
        else:
            sign = 1

        x *= sign
        digits = []

        while x:
            digits.append(digs[int(x % base)])
            x = int(x / base)

        if sign < 0:
            digits.append('-')

        digits.reverse()

        return ''.join(digits)

    def encode(self):
        y = []
        m = self.int2base(self.m, self.p)
        for i in range(1,self.n + 1):
            p = self.poly([int(j) for j in m], i)
            y.append(p)
        return y
k = 3
s = 1
n = k + 2 * s
p = 11
m = 29
reedsolomon = ReedSolomon(k, s, p, m)
print(reedsolomon.encode())

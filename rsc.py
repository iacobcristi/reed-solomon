import string
digs = string.digits + string.ascii_letters

k = 3
s = 1
n = k + 2 * s
p = 11
m = 29

def poly(a_list, x):
        ans = 0
        p = k - 1
        for a in a_list:
            ans += (a*x**p) % 11
            p = p - 1
        return ans % 11

def int2base(x, base):
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
y = []
m = int2base(m,p)
for i in range(1,n+1):
    p = poly([int(j) for j in m], i)
    y.append(p)

print(y)
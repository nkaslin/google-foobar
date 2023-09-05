

    



    

def solution(grid):
    def extract_relevant(x, y, z):
        ...

    def count(yy, zz):
        if yy == 0:
            b = zz & 3
            return b.bit_count()
        b = 0
        b |= zz & (1 << yy)
        b |= zz & (1 << (yy + 1))
        b |= zz & (1 << (n + 1))
        return b.bit_count()

    def is_possible(xx, yy, zz, extra):
        tot = count(yy, zz) + extra
        return not (grid[yy][xx] ^ (tot == 1))
    
    m, n = len(grid), len(grid[0])
    cache = [[[-1 for _ in range(1 << (m + 2))] for _ in range(n)] for _ in range(m)]

    def dp(x, y, z):
        if cache[x][y][z] != -1:
            return cache[x][y][z]
        cnt = count(y, z, n)
        if grid[y][x]:
            if cnt > 1:
                cache[x][y][z] = 0
                return 0



if __name__ == "__main__":

    a = 0b10100110011
    print(count(1, a, 9))

    b = 0b00100110010
    print(count(0, b, 9))


"""
y|x ->
|  0 ...01   ka
v  1 ...11   lb
   2 ...0    c
   3 ...0    d
   4 ...1    e
   5 ...1    f
   6 ...0    g
   7 ...0    h
   8 ...1    i
   9 ...0    j

1 0100110011
l jihgfedcba
"""

"""


"""


def extract_relevant(x, y, z):
    ...

def count(y, z, n):
    if y == 0:
        b = z & 3
        return b.bit_count()
    b = 0
    b |= z & (1 << y)
    b |= z & (1 << (y + 1))
    b |= z & (1 << (n + 1))
    return b.bit_count()


    

def solution(grid):
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


def solution(grid):

    def count(y, z):
        if y == 0:
            b = z & 3
            return b.bit_count()
        b = 0
        b |= z & (1 << y)
        b |= z & (1 << (y + 1))
        b |= z & (1 << (n + 1))
        return b.bit_count()

    def is_possible(x, y, z, extra):
        tot = count(y, z) + extra
        return not (grid[y][x] ^ (tot == 1))
    
    def set_bit(z, pos, new_bit):
        # sets bit in binary number z at pos to new_bit and returns new number
        mask = 1 << pos
        v = z
        v &= ~mask
        if new_bit:
            v |= mask
        return v 
    
    def next_states(x, y, z, is_true, cnt):
        if y == m - 1:
            next_y = 0
            next_x = x + 1
        else:
            next_y = y + 1
            next_x = x
        if is_true:
            if cnt == 1:
                extra_bit = z & (1 << (y + 1))
                new_z = z 
                next_zs = []
        # TODO: handle all other cases

        
        
        
    
    m, n = len(grid), len(grid[0])
    cache = [[[-1 for _ in range(1 << (m + 2))] for _ in range(n)] for _ in range(m)]

    def dp(x, y, z):
        if cache[x][y][z] != -1:
            return cache[x][y][z]
        cnt = count(y, z)
        if grid[y][x]:
            if cnt > 1:
                cache[x][y][z] = 0
                return 0
            if cnt == 0:




if __name__ == "__main__":
    ...

    # a = 0b10100110011
    # print(count(1, a, 9))

    # b = 0b00100110010
    # print(count(0, b, 9))


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


def solution(grid):

    def count(y, z):
        cnt = 0
        if z & (1 << y):
            cnt += 1
        if z & (2 << y):
            cnt += 1
        if z & (1 << extra_bit_position):
            cnt += 1
        return cnt
        # b = z & (3 << y)
        # return bin(b).count("1")  # b.bit_count()

    def post_check(x, y, z, is_extra):
        # returns if the current occupations are permitted
        tot = count(y, z) + int(is_extra)
        return not (grid[y][x] ^ (tot == 1))
    
    # def post_check_2(x, y, z, is_extra):
    #     # returns if the current occupations are permitted
    #     tot = count(y, z) + int(is_extra)
    #     return not (grid[y][x] ^ (tot == 1))
    
    def pre_check(x, y, z):
        if not grid[y][x]: return True
        return count(y, z) < 2
    
    def get_extra_bit(z):
        return z & (1 << extra_bit_position) != 0
    
    def set_bit(z, pos, new_bit):
        # sets bit in binary number z at pos to new_bit and returns new number
        mask = 1 << pos
        v = z
        v &= ~mask
        if new_bit:
            v |= mask
        return v 
    
    def get_next_states(x, y, z):
        # returns a list of possible next states
        if y == m - 1:
            next_y = 0
            next_x = x + 1
        else:
            next_y = y + 1
            next_x = x
        # if y == m - 1:
        #     next_extra_bit = z & 1 != 0
        # else:
        next_extra_bit = z & (1 << (y + 1)) != 0
        if y == 0:
            next_zs = [set_bit(z, extra_bit_position, next_extra_bit) for _ in range(4)]
            next_zs = [set_bit(nz, y, nb) for nz, nb in zip(next_zs, [0, 1, 0, 1])]
            next_zs = [set_bit(nz, y + 1, nb) for nz, nb in zip(next_zs, [0, 0, 1, 1])]
        else:
            next_zs = [set_bit(z, extra_bit_position, next_extra_bit) for _ in range(2)]
            next_zs = [set_bit(nz, y + 1, nb) for nz, nb in zip(next_zs, [0, 1])]
        if x == 0:
            next_zs = [set_bit(nz, extra_bit_position, 0) for nz in next_zs]
            next_zs += [set_bit(nz, extra_bit_position, 1) for nz in next_zs]
        return [(next_x, next_y, nz) for nz in next_zs]


    def dp(x, y, z):
        if x == n:
            return 1
        # print x, y, z
        # print(cache[x][y][z])
        if cache[x][y][z] != -1:
            return cache[x][y][z]
        # # terminal condition
        # if x == n:
        #     return 1
        if not pre_check(x, y, z):
            cache[x][y][z] = 0
            return 0
        res = 0
        extra_bit_tmp = get_extra_bit(z)
        # current = z & (1 << y)
        next_states = get_next_states(x, y, z)
        for nx, ny, nz in next_states:
            if not post_check(x, y, nz, extra_bit_tmp):
            # if not post_check_2(x, y, nz, current):
                continue
            res += dp(nx, ny, nz)
        cache[x][y][z] = res
        return res 
    
    

    m, n = len(grid), len(grid[0])
    extra_bit_position = m + 1

    cache = [[[-1 for _ in range((1 << (m + 2)) )] for _ in range(m + 1)] for _ in range(n)]

    # cache[n][0] = [1 for _ in range((1 << (m + 2)))]

    # print(len(cache), len(cache[0]), len(cache[0][0]))

    

    res = dp(0, 0, 0) + dp(0, 0, 1 << extra_bit_position)
    # res = dp(0, 0, 1 << extra_bit_position)
    print(cache)

    return res


if __name__ == "__main__":
    # grid = [[True, False, True], [False, True, False], [True, False, True]]  # 4
    # grid = [[True]]  # 4
    # grid = [[False]]  # 12
    # grid = [[True], [True]]
    # grid = [[True], [False]]
    # grid = [[True, False], [False, True]]
    # grid = [[True, False, True, False, False, True, True, True], [True, False, True, False, False, False, True, False], [True, True, True, False, False, False, True, False], [True, False, True, False, False, False, True, False], [True, False, True, False, False, True, True, True]]
    # 254
    # grid = [[True, True, False, True, False, True, False, True, True, False], [True, True, False, False, False, False, True, True, True, False], [True, True, False, False, False, False, False, False, False, True], [False, True, False, False, False, False, True, True, False, False]]
    # 11567
    grid = [[True, True, True]]  # 8
    # grid = [[True], [True], [True]]  # 

    res = solution(grid)
    # print "- " * 20
    print(res)



    # a = 0b10100110011
    # print bin(a).count("1")

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

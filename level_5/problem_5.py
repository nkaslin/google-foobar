
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

    def post_check(x, y, z, is_extra):
        # returns if the current occupations are permitted
        tot = count(y, z) + int(is_extra)
        return not (grid[y][x] ^ (tot == 1))

    def pre_check(x, y, z):
        if not grid[y][x]:
            return True
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
        next_extra_bit = z & (1 << (y + 1)) != 0
        if y == 0:
            next_zs = [set_bit(z, extra_bit_position, next_extra_bit)
                       for _ in range(4)]
            next_zs = [set_bit(nz, y, nb)
                       for nz, nb in zip(next_zs, [0, 1, 0, 1])]
            next_zs = [set_bit(nz, y + 1, nb)
                       for nz, nb in zip(next_zs, [0, 0, 1, 1])]
        else:
            next_zs = [set_bit(z, extra_bit_position, next_extra_bit)
                       for _ in range(2)]
            next_zs = [set_bit(nz, y + 1, nb)
                       for nz, nb in zip(next_zs, [0, 1])]
        if x == 0:
            next_zs = [set_bit(nz, extra_bit_position, 0) for nz in next_zs]
            next_zs += [set_bit(nz, extra_bit_position, 1) for nz in next_zs]
        return [(next_x, next_y, nz) for nz in next_zs]

    def dp(x, y, z):
        if x == n:
            return 1
        if cache[x][y][z] != -1:
            return cache[x][y][z]
        if not pre_check(x, y, z):
            cache[x][y][z] = 0
            return 0
        res = 0
        extra_bit_tmp = get_extra_bit(z)
        next_states = get_next_states(x, y, z)
        for nx, ny, nz in next_states:
            if not post_check(x, y, nz, extra_bit_tmp):
                continue
            if ny == 0:
                nz = set_bit(nz, extra_bit_position, nz & 1)
                nz = set_bit(nz, 0, 0)

            res += dp(nx, ny, nz)
        cache[x][y][z] = res
        return res

    if grid == [[]]:
        return 2

    m, n = len(grid), len(grid[0])
    extra_bit_position = m + 1

    cache = [[[-1 for _ in range((1 << (m + 2)))]
              for _ in range(m + 1)] for _ in range(n)]

    res = dp(0, 0, 0) + dp(0, 0, 1 << extra_bit_position)

    return res


if __name__ == "__main__":
    # test case 1
    grid = [[True, False, True], [False, True, False], [True, False, True]]
    output = 4
    assert solution(grid) == output

    # test case 2
    grid = [[True, False, True, False, False, True, True, True],
            [True, False, True, False, False, False, True, False],
            [True, True, True, False, False, False, True, False],
            [True, False, True, False, False, False, True, False],
            [True, False, True, False, False, True, True, True]]
    output = 254
    assert solution(grid) == output

    # test case 3
    grid = [[True, True, False, True, False, True, False, True, True, False],
            [True, True, False, False, False, False, True, True, True, False],
            [True, True, False, False, False, False, False, False, False, True],
            [False, True, False, False, False, False, True, True, False, False]]
    output = 11567
    assert solution(grid) == output

    # test case 4
    grid = [[True]]
    output = 4
    assert solution(grid) == output

    # test case 5
    grid = [[False]]
    output = 12
    assert solution(grid) == output

    # test case 6
    grid = [[True, True, True]]
    output = 8
    assert solution(grid) == output

    # test case 7
    grid = [[True], [True], [True]]
    output = 8
    assert solution(grid) == output

    # test case 8
    grid = [[True for _ in range(50)] for _ in range(9)]
    output = 100663356
    assert solution(grid) == output

    # test case 9
    grid = [[False for _ in range(50)] for _ in range(9)]
    output = 342015522530891220930318205106520120995761507496882358868830383880718255659276117597645436150624945088901216664965365050
    assert solution(grid) == output

    # test case 10
    grid = [[]]
    output = 2
    assert solution(grid) == output

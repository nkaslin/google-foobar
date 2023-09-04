import numpy as np
from fractions import Fraction
from numpy.linalg import inv


def get_absorbing_states(m):
    absobing_states = []
    for i, row in enumerate(m):
        if sum(row) == 0:
            absobing_states.append(i)
    return absobing_states

def replace_with_probabilities(m):
    for i, row in enumerate(m):
        sm = sum(row)
        for j in range(len(row)):
            if m[i][j] == 0:
                continue
            m[i][j] = float(m[i][j]) / sm
    
def get_Q(m, absorbing_states):
    Q = []
    for i, row in enumerate(m):
        if i in absorbing_states:
            continue
        Q.append([])
        for j in range(len(row)):
            if j in absorbing_states:
                continue
            Q[-1].append(m[i][j])
    return Q

def get_P(m, absorbing_states):
    P = []
    for i, row in enumerate(m):
        if i in absorbing_states:
            continue
        P.append([])
        for j in range(len(row)):
            if j not in absorbing_states:
                continue
            P[-1].append(m[i][j])
    return P

def solution(m):
    if m == [[0]]:
        return [1, 1]
    
    absorbing_states = get_absorbing_states(m)

    replace_with_probabilities(m)

    Q = get_Q(m, absorbing_states)
    R = get_P(m, absorbing_states)

    m = np.matrix(m)
    Q = np.matrix(Q)
    R = np.matrix(R)

    I = np.identity(len(Q))

    N = inv(I - Q)
    
    B = N * R

    res_fracs = [Fraction(B[0,i]).limit_denominator() for i in range(B.shape[1])]
    denoms = [x.denominator for x in res_fracs]
    lcm = np.lcm.reduce(denoms)
    
    res = [int(np.round(x.numerator * (lcm / x.denominator))) for x in res_fracs] + [lcm]
    return res


if __name__ == "__main__":

    m1 = [[0, 2, 1, 0, 0],
          [0, 0, 0, 3, 4],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0]]
    assert solution(m1) == [7, 6, 8, 21]

    m2 = [[0, 1, 0, 0, 0, 1],
          [4, 0, 0, 3, 2, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0]]
    assert solution(m2) == [0, 3, 2, 9, 14]

    m3 = [[0,0,0,0],
         [1,0,1,0],
         [0,1,0,0],
         [0,0,1,3]]
    assert solution(m3) == [1, 1]
    
    m4 = [[0]]
    assert solution(m4) == [1, 1]

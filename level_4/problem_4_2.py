from collections import defaultdict


def solution(banana_list):

    def gcd(x, y):
        while y != 0:
            x, y = y, x % y
        return x

    def is_valid(x, y):
        if not x or not y: 
            return True
        sm = x + y
        gcd_1 = gcd(x, y)
        gcd_2 = 0
        while x != y and gcd_1 != gcd_2:
            if x > y:
                x, y = y, x
            if sm / gcd_1 in squares:
                return False
            y -= x
            x *= 2
            gcd_2 = gcd_1
            gcd_1 = gcd(x, y)
        return gcd_1 == gcd_2
    
    squares = {1 << i for i in range(32)}

    graph = defaultdict(set)
    n = len(banana_list)
    for i in range(n):
        for j in range(i + 1, n):
            if is_valid(banana_list[i], banana_list[j]):
                graph[i].add(j)
                graph[j].add(i)

    found = True
    res = n
    removed = set()
    while found:
        counts = [(len(x), i) for i, x in graph.items()]
        counts.sort()
        first, second = None, None
        for ln, node in counts:
            if node in removed or ln == 0:
                continue
            if first is None:
                first = node
            elif node in graph[first]:
                second = node
                res -= 2
                break

        if first is None or second is None:
            return res
            
        removed.add(first)
        removed.add(second)
        
        for node in range(n):
            if first in graph[node]:
                graph[node].remove(first)
            if second in graph[node]:
                graph[node].remove(second)
                
    return res
    

if __name__ == "__main__":
    assert solution([1,7,3,21,13,19]) == 0

    assert solution([1,1]) == 2

    assert solution([688, 673, 440, 360, 380, 514, 332, 187, 263, 647, 671]) == 1

    assert solution([1,1,1,2]) == 2

    assert solution([1,1,1,1,1,3,1]) == 7

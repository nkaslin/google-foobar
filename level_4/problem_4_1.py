from collections import deque


def simplify_graph(entrances, exits, path):
    n = len(path)
    new_n = n - len(exits) - len(entrances) + 2
    new_path = [[0 for _ in range(new_n)] for _ in range(new_n)]
    mp = {}
    cur = 1
    for i in range(n):
        if i in entrances:
            mp[i] = 0
        elif i in exits:
            mp[i] = new_n - 1
        else:
            mp[i] = cur
            cur += 1
    for i, row in enumerate(path):
        for j in range(len(row)):
            new_path[mp[i]][mp[j]] += path[i][j]
    return new_path


def bfs(graph, reverse_graph):
    n = len(graph)
    last = [-1 for _ in range(n)]

    found = False
    q = deque([0])
    while q:
        node = q.popleft()
        for i in range(1, n):
            if graph[node][i] != 0 and last[i] == -1:
                last[i] = node
                if i == n - 1:
                    found = True
                    break
                q.append(i)
            if reverse_graph[node][i] != 0 and last[i] == -1:
                last[i] = node
                if i == n - 1:
                    found = True
                    break
                q.append(i)
        if found:
            break

    if not q and not found:
        return None

    # reconstruct path
    cur_node = n - 1
    path = [n - 1]
    while cur_node != 0:
        cur_node = last[cur_node]
        path.append(cur_node)
    return path[::-1]


def solution(entrances, exits, path):

    graph = simplify_graph(set(entrances), set(exits), path)
    n = len(graph)

    reverse_graph = [[0 for _ in range(n)] for _ in range(n)]

    res = 0
    while True:
        pth = bfs(graph, reverse_graph)

        if not pth:
            return res

        # get bottleneck value
        bottleneck = float("inf")
        for x, y in zip(pth, pth[1:]):
            if graph[x][y] > 0:
                bottleneck = min(bottleneck, graph[x][y])
            elif reverse_graph[x][y] > 0:
                bottleneck = min(bottleneck, reverse_graph[x][y])

        res += bottleneck

        # update graph and reverse_graph
        for x, y in zip(pth, pth[1:]):
            if graph[x][y] > 0:
                graph[x][y] -= bottleneck
                reverse_graph[y][x] += bottleneck
            elif reverse_graph[x][y] > 0:
                graph[y][x] += bottleneck
                reverse_graph[x][y] -= bottleneck


if __name__ == "__main__":
    # test case 1
    entrances = [0]
    exits = [3]
    path = [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]
    output = 6
    assert solution(entrances, exits, path) == output

    # test case 2
    entrances = [0, 1]
    exits = [4, 5]
    path = [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4],
            [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    output = 16
    assert solution(entrances, exits, path) == output

    # test case 3
    entrances = [0]
    exits = [3]
    path = [[0, 100, 100, 0], [0, 0, 1, 100], [0, 0, 0, 100], [0, 0, 0, 0]]
    output = 200
    assert solution(entrances, exits, path) == output

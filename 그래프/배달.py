def solution(N, road, K):
    answer = 1
    graph = [[] for _ in range(N + 1)]
    for a, b, c in road:
        graph[a].append([b, c])
        graph[b].append([a, c])

    dist = [1e9] * (N + 1)
    tree = []
    tree.append([1, 0])
    dist[0] = 0
    dist[1] = 0

    while tree:
        n, ncost = tree.pop()
        print(n, ncost)
        for nv, cost in graph[n]:
            if cost + ncost < dist[nv]:
                dist[nv] = cost + ncost
                tree.append([nv, dist[nv]])
    print(dist)

    for i in dist:
        if 0 < i <= K:
            answer += 1
    return answer

if __name__ == '__main__':
    N = 5
    road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
    K = 3
    print(solution(N, road, K))
def dfs_iterative(graph_, v, visited):
    print(v + 1, end=' ')
    visited[v], stack = True, [v]
    while stack:
        for i in graph_[stack[-1]]:
            if not visited[i]:
                print(i + 1, end=' ')
                visited[i] = True
                stack.append(i)
                break
        else:
            stack.pop()


def dfs_recursive(graph_, v, visited):
    print(v + 1, end=' ')
    visited[v] = True
    for i in graph_[v]:
        if not visited[i]:
            dfs_recursive(graph_, i, visited)


graph = [[1, 2, 7], [0, 6], [0, 3, 4], [2, 4], [2, 3], [6], [1, 5, 7], [0, 6]]
dfs_iterative(graph, 0, [False] * 8)
print()
dfs_recursive(graph, 0, [False] * 8)
print()

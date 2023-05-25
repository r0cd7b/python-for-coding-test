def dfs_iterative(graph_, v, visited_):
    stack, visited_[v] = [v], True
    print(v + 1, end=' ')
    while stack:
        v = stack[-1]
        for i in graph_[v]:
            if not visited_[i]:
                stack.append(i)
                visited_[i] = True
                print(i + 1, end=' ')
                break
        else:
            stack.pop()


def dfs_recursive(graph_, v, visited_):
    print(v + 1, end=' ')
    visited_[v] = True
    for i in graph_[v]:
        if not visited_[i]:
            dfs_recursive(graph_, i, visited_)


graph = [[1, 2, 7], [0, 6], [0, 3, 4], [2, 4], [2, 3], [6], [1, 5, 7], [0, 6]]
dfs_iterative(graph, 0, [False] * 8)
print()
dfs_recursive(graph, 0, [False] * 8)
print()

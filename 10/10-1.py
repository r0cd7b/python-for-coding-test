# 기본적인 서로소 집합 알고리즘 소스코드
def find_parent(parent, x):
    if parent[x] < x:
        return find_parent(parent, parent[x])
    return x

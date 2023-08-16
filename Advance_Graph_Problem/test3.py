import fileinput
import random


def find(parents, i):
    r = i
    while r in parents:
        r = parents[r]
    while i in parents:
        p = parents[i]
        parents[i] = r
        i = p
    return i


def unite(parents, i, j):
    parents[i] = j


def karger(n, edges):
    edges = list(edges)
    random.shuffle(edges)
    parents = {}
    for i, j in edges:
        if n <= 2:
            break
        i = find(parents, i)
        j = find(parents, j)
        if i == j:
            continue
        unite(parents, i, j)
        n -= 1
    return sum(find(parents, i) != find(parents, j) for (i, j) in edges)


def main():
    lines = list(fileinput.input())
    n = len(lines)
    edges = set()
    for line in lines:
        fields = iter(map(int, line.split()))
        u = next(fields)
        edges.update((min(u, v), max(u, v)) for v in fields)
    print(min(karger(n, edges) for k in range(1000)))


if __name__ == "__main__":
    main()
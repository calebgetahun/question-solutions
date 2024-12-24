def computer_network(n, nodes: list):
    route = [n]
    just_visited = n - 2
    while just_visited >= 0:
        route.append(nodes[just_visited])
        just_visited = nodes[just_visited] - 2
    return " ".join(map(str, reversed(route)))

if __name__ == "__main__":
    n = int(input())
    nodes = list(map(int, input().split(" ")))
    print(computer_network(n, nodes))

# TC: O(N)
# SC: O(N)
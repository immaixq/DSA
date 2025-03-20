from collections import deque

def bfs(graph, start):
    visited = set([start]) # keep track of visited nodes
    queue = deque([start])
    distance = {start: 0}

    while queue:
        node = queue.popleft()
        print("Visiting node:", node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor) # mark as visited
                queue.append(neighbor) # add to queue
                distance[neighbor] = distance[node] + 1 # update distance

    return distance

if __name__ == "__main__":
    graph = {
        "A": ["B", "C", "D", "E"],
        "B": ["F"],
        "C": [],
        "D": ["G"],
        "E": [],
        "F": ["H"],
        "G": ["I"],
        "H": [],
        "I": []
    }

    start = "A"
    distances = bfs(graph, start)
    print("Distances from", start, ":", distances)
class Network:
    def __init__(self):
        self.graph = {} 

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, node1, node2):
        if node1 not in self.graph:
            self.add_node(node1)
        if node2 not in self.graph:
            self.add_node(node2)

        # append both for bidirectional
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    def remove_edge(self, node1, node2):
        if node1 in self.graph and node2 in self.graph:
            self.graph[node1].remove(node2)
            self.graph[node2].remove(node1)

    def remove_node(self, node):
        if node in self.graph:
            for neighbor in self.graph[node]:
                self.graph[neighbor].remove(node)
            del self.graph[node]

    def get_connections(self, node):
        if node in self.graph:
            return self.graph[node]
        else:
            return []
        
    def __str__(self):
        return (f"{node}: {self.graph[node]}" for node in self.graph)

if __name__ == "__main__":
    network = Network()
    network.add_node("Alibaba")
    network.add_node("Baba")
    network.add_node("AMAZ")
    network.add_edge("Alibaba", "Baba")
    network.add_edge("Alibaba", "AMAZ")
    network.remove_edge("Alibaba", "Baba")
    network.remove_node("Baba")
    print(network.get_connections("Alibaba"))
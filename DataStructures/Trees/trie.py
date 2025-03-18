import graphviz


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        """Inserts a word into the trie."""
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end_of_word = True

    def search(self, word: str):
        """Returns True if the word exists in the trie, False otherwise."""
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end_of_word

    def startsWith(self, prefix: str):
        """Returns True if there is any word in the trie that starts with the given prefix."""
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

    def _dfs(self, node, current_prefix, result):
        """Depth-first search to find words in trie that start with a prefix."""
        if node.is_end_of_word:
            result.append(current_prefix)

        for ch, child_node in node.children.items():
            self._dfs(child_node, current_prefix + ch, result)

    def getWordsWithPrefix(self, prefix: str):
        """Returns a list of words in the trie that start with the given prefix."""
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]

        result = []
        self._dfs(node, prefix, result)
        return result

    def _generate_graph(self, node: TrieNode, graph: graphviz.Digraph, parent: str):
            """Generates the graph recursively for visualization."""
            if node is None:
                return
            
            for ch, child_node in node.children.items():
                node_name = f"{parent}_{ch}"
                graph.node(node_name, label=ch, shape="ellipse", style="filled", fillcolor="lightyellow")
                # Draw an edge between parent and child
                graph.edge(parent, node_name, label=ch)
                self._generate_graph(child_node, graph, node_name)

    def visualise(self):
        """Generates and saves a graphical representation of the Trie."""
        graph = graphviz.Digraph(format="png", engine="dot")
        
        # Root node definition
        graph.node("root", label="Root", shape="ellipse", style="filled", fillcolor="lightgray")

        # Generate the graph starting from the root
        self._generate_graph(self.root, graph, "root")
        
        graph.render("trie_visualization", cleanup=True)

# Example usage
trie = Trie()

# Insert words into the trie
trie.insert("banana")
trie.insert("bat")
trie.insert("ball")
trie.insert("batman")
trie.insert("ab")
trie.insert("abcd")

# Get words with a prefix
print(trie.getWordsWithPrefix("ba"))  # ['banana', 'bat', 'ball', 'batman']

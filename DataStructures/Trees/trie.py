import graphviz


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        # create node from each character
        node = self.root
        for ch in word:
            if ch not in node.children:
                # create node if new
                node.children[ch] = TrieNode()
            # move to the next node
            node = node.children[ch]
        # The end of the word
        node.is_end_of_word = True

    def search(self, word: str):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False  # cant find ch
            # move to the next node
            node = node.children[ch]
        return node.is_end_of_word

    def startsWith(self, prefix: str):
        node = self.root
        for ch in prefix:
            if ch not in node.children():
                return False
            node = node.children[ch]
        return True

    def _dfs(self, node, current_prefix, result):
        """
        dfs to find words in trie that starts with a prefix
        """
        if node.is_end_of_word():
            result.append(current_prefix)

        for ch, child_node in node.children.items():
            self._dfs(child_node, current_prefix + ch, result)

    def getWordsWithPrefixs(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return []

        result = []
        self._dfs(node, prefix, result)

    def _generate_graph(self, node, graph, parent, label):
        if node is None:
            return

        node_name = label
        graph.node(node_name, label)

        if parent is not None:
            graph.edge(parent, node_name)

        for ch, child_node in node.children.items():
            self._generate_graph(child_node, graph, node_name, node_name + "-" + label)

    def visualise(self):
        """Generates a graphical representation of the Trie."""
        graph = graphviz.Digraph(format="png", engine="dot")
        graph.node(
            "root", label="Root", shape="ellipse", style="filled", fillcolor="lightgray"
        )

        self._generate_graph(self.root, graph, "root", "root")

        # Render the graph to a PNG file
        graph.render("trie_visualization", cleanup=True)


# Example usage
trie = Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("banana")
trie.insert("bat")
trie.insert("ball")
trie.insert("batman")

# Visualize the Trie
trie.visualise()

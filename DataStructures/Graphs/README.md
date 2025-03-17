## Graphs

Graph:: Data structure that specialises in relationships which tells how data is connected, for example the Facebook network 
- Each person is a node called vertex
- Each friendship, the connected line is called an edge
- Vertex connected by an edge is said to be adjacent 

### Meta VS X Network
The difference between Facebook network v.s X network is that the relationship in Facebook is mutual while X is one directional. For one directional graph, it's called **directed graph** while mutual connection is **non-directed graph**

## Graph Traversal 
There are two classic ways of walking through the graphs:
1. Breadth First Search
2. Depth First Search

### Breadth First Search
The breadth first search algorithm uses queue to keep track of which vertices to handle next. Say for example this is a simple friendship network: Lily -> Huai -> Alex, Alex is said to be Lily's second degree connection. We can use breadth first search to determine nth degree connection of Alice where the queue is used to store Alice's connection, and the order of the queue represents the number of degree. 



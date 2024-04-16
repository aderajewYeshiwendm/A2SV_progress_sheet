class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        all_nodes = set(range(n))
    
    # Initialize a set to store nodes with incoming edges
        with_incoming_edges = set()

        # Iterate through the edges to find nodes with incoming edges
        for _, to_node in edges:
            with_incoming_edges.add(to_node)

        # Find the difference between all nodes and nodes with incoming edges
        # This gives us the nodes without incoming edges
        result = all_nodes - with_incoming_edges

        # Convert the result set to a list and return it
        return list(result)
        
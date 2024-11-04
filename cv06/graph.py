import numpy as np


class Graph:
    """
    A structure that represents a graph. It has two representations:
    adjacency matrix and probability transition matrix.
    """

    def __init__(self, edges: list[tuple[int, int]]) -> None:
        self.adjacency_matrix = None
        self.prob_transition_matrix = None
        self.__init_adjacency_matrix(edges=edges)
        self.__init_prob_transition_matrix()

    def __init_adjacency_matrix(self, edges):
        # Find maximum node (number) to allocate enough len numpy.array
        max_node = max(max(node1, node2) for node1, node2 in edges)
        # Allocate with zero values
        self.adjacency_matrix = np.zeros((max_node, max_node), dtype=int)
        
        for node1, node2 in edges:
            self.adjacency_matrix[node1-1][node2-1] = 1

    def __init_prob_transition_matrix(self):
        # Creates copy of the adjacency matrix
        self.prob_transition_matrix = np.copy(self.adjacency_matrix).astype('float')
        # Per row in matrix:
        for row_i, row in enumerate(self.prob_transition_matrix):
            count = np.sum(row)
            if count:
                self.prob_transition_matrix[row_i] /= count

    
    @classmethod
    def read_edges_from_file(cls, file_obj) -> list[tuple[int, int]]:
        edges = []
        for line in file_obj:
            # Split line ("1, 2") into two nodes and convert to int
            node1, node2 = map(int, line.strip().split(','))
            edges.append((node1, node2))
        return edges

    
        

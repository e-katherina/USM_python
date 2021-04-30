from __future__ import annotations
from typing import *

import numpy as np
import numpy.typing as npt


class Graf:
    """
    This class was designed for convenient handling of graphs
    You should initialize object of type Graf with adjacency matrix using set_adiacenta method
    After that you can get adjacency, incidence and kirhoff matrix
    Also it can unite two random graphs via get_united_graph function
    """
    def __init__(self):
        self.M_adiacenta = None
        self.nodes = None
        self.edges = None
        
    def get_nodes(self) -> int:
        """
        :return: number of nodes
        """
        nodes = self.M_adiacenta.shape[0]
        return nodes
    
    def get_edges(self) -> int:
        """
        :return: number of edges
        """
        edges = (np.sum(self.M_adiacenta) + np.trace(self.M_adiacenta))/2
        return int(edges)
    
    def set_adiacenta(self, M_adiacenta: npt.ArrayLike):
        """
        :param M_adiacenta: adjacency matrix
        """
        self.M_adiacenta = M_adiacenta.astype('int')
        self.nodes = self.get_nodes()
        self.edges = self.get_edges()
    
    def get_adiacenta(self) -> npt.ArrayLike:
        """
        :return: adjacency matrix
        """
        return self.M_adiacenta
        
    def get_incidenta(self) -> npt.ArrayLike:
        """
        :return: incidence matrix
        """
        M_incidenta = np.array([]).reshape(self.nodes, 0)
        for i in range(self.nodes):
            for j in range(i, self.nodes):
                if self.M_adiacenta[i, j]:
                    v = np.zeros((self.nodes, 1))
                    v[[i, j], 0] = self.M_adiacenta[i, j]
                    M_incidenta = np.hstack((M_incidenta, v))
                
        return M_incidenta.astype('int')
    
    def get_kirhoff(self) -> npt.ArrayLike:
        """
        :return: kirhoff matrix
        """
        M_kirhoff = -self.M_adiacenta
        for i in range(self.nodes):
            M_kirhoff[i, i] = np.sum(self.M_adiacenta[i])
        return M_kirhoff.astype('int')
    
    def get_united_graph(A: Type[Graf], B: Type[Graf]) -> Type[Graf]:
        """
        Merge two graphs into one
        :param A: first graph
        :param B: second graph
        :return: united graph
        """
        C_nodes = A.get_nodes() + B.get_nodes()

        C_adiacenta = np.ones((C_nodes, C_nodes))
        C_adiacenta[:A.get_nodes(), :A.get_nodes()] = A.get_adiacenta()
        C_adiacenta[-B.get_nodes():, -B.get_nodes():] = B.get_adiacenta()
        
        C = Graf()
        C.set_adiacenta(C_adiacenta)
        return C

    def get_min_edge(self, nodes, M_incidenta):
        edges = M_incidenta[:, np.unique(np.nonzero(M_incidenta[nodes])[1])]
        values = np.delete(edges, nodes, axis=0)
        edge = np.where(values > 0, values, np.inf).argmin() % values.shape[1]
        return edges[:, [edge]]

    def get_arbore_partial_min(self):
        """
        :return: Incidence matrix of minimal partial tree
        """
        M_incidenta = self.get_incidenta()
        M_partial_incidenta = np.array([]).reshape(self.nodes, 0)
        nodes = [0]

        for _ in range(self.nodes - 1):
            edge = self.get_min_edge(nodes, M_incidenta)
            M_partial_incidenta = np.hstack((M_partial_incidenta, edge))
            new_node = set(np.nonzero(edge)[0].flatten()) - set(nodes)
            nodes.extend(new_node)

        return M_partial_incidenta

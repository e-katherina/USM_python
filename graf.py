from __future__ import annotations
from typing import *

import numpy as np
import numpy.typing as npt


class Graf:
    
    def __init__(self):
        self.M_adiacenta = None
        self.nodes = None
        self.edges = None
        
    def get_nodes(self) -> int:
        '''
        :return: number of nodes
        '''
        nodes = self.M_adiacenta.shape[0]
        return nodes
    
    def get_edges(self) -> int:
        '''
        :return: number of edges
        '''
        edges = (np.sum(self.M_adiacenta) + np.trace(self.M_adiacenta))/2
        return int(edges)
    
    def set_adiacenta(self, M_adiacenta: npt.ArrayLike):
        '''
        :param M_adiacenta: adjacency matrix
        '''
        self.M_adiacenta = M_adiacenta
        self.nodes = self.get_nodes()
        self.edges = self.get_edges()
    
    def get_adiacenta(self) -> npt.ArrayLike:
        '''
        :return: adjacency matrix
        '''
        return self.M_adiacenta
        
    def get_incidenta(self) -> npt.ArrayLike:
        '''
        :return: incidence matrix
        '''
        M_incidenta = np.array([]).reshape(self.nodes, 0)
        for i in range(self.nodes):
            for j in range(i, self.nodes):
                if self.M_adiacenta[i, j] == 1:
                    v = np.zeros((self.nodes, 1))
                    v[[i, j], 0] = 1
                    M_incidenta = np.hstack((M_incidenta, v))
                
        return M_incidenta
    
    def get_kirhoff(self) -> npt.ArrayLike:
        '''
        :return: kirhoff matrix
        '''
        M_kirhoff = -self.M_adiacenta
        for i in range(self.nodes):
            M_kirhoff[i, i] = np.sum(self.M_adiacenta[i])
        return M_kirhoff
    
    def get_united_graph(A: Type[Graf], B: Type[Graf]) -> Type[Graf]:
        '''
        Merge two graphs into one
        :param A: first graph
        :param B: second graph
        :return: united graph
        '''
        A_adiacenta = A.get_adiacenta()
        B_adiacenta = B.get_adiacenta()
        
        A_nodes = A.get_nodes()
        B_nodes = B.get_nodes()
        C_nodes = A_nodes + B_nodes
        C_adiacenta = np.ones((C_nodes, C_nodes))
        C_adiacenta[:A_nodes, :A_nodes] = A_adiacenta
        C_adiacenta[-B_nodes:, -B_nodes:] = B_adiacenta
        
        C = Graf()
        C.set_adiacenta(C_adiacenta)
        return C

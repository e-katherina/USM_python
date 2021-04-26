import numpy as np


class Graf:
    
    def __init__(self):
        self.M_adiacenta = None
        self.nodes = None
        self.edges = None
        
    def get_nodes(self):
        nodes = self.M_adiacenta.shape[0]
        return nodes
    
    def get_edges(self):
        edges = (np.sum(self.M_adiacenta) + np.trace(self.M_adiacenta))/2
        return int(edges)
    
    def set_adiacenta(self, M_adiacenta):
        self.M_adiacenta = M_adiacenta
        self.nodes = self.get_nodes()
        self.edges = self.get_edges()
    
    def get_adiacenta(self):
        return self.M_adiacenta
        
    def get_incidenta(self):
        M_incidenta = np.array([]).reshape(self.nodes, 0)
        for i in range(self.nodes):
            for j in range(i, self.nodes):
                if self.M_adiacenta[i, j] == 1:
                    v = np.zeros((self.nodes, 1))
                    v[[i, j], 0] = 1
                    M_incidenta = np.hstack((M_incidenta, v))
                
        return M_incidenta
    
    def get_kirhoff(self):
        M_kirhoff = -self.M_adiacenta
        for i in range(self.nodes):
            M_kirhoff[i, i] = np.sum(self.M_adiacenta[i])
        return M_kirhoff
    
    def get_united_graph(A, B):
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

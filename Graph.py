from Nodes import Nodes

class Graph:
    """ 
    Attributes 
    ----------
        > num_nodes : number of nodes
        > num_edges : number of edges
        > nodes :   list of nodes
        > edges :   list of edges
        > labels    : list of labels of nodes
    """

    def __init__(self):
        self.num_nodes = 0
        self.num_edges = 0
        self.nodes = []
        self.edges = []
        self.labels = []

    def addNode(self, label):
        """
        Adding a new node into the graph

        Parameter
        ---------
            > label:  String that labels a node
        """
        if label in self.labels:
            raise Exception('The node already exist')


        newnode = Nodes(label)
        self.num_nodes = self.num_nodes + 1
        self.nodes.append(newnode)
        self.labels.append(label)
    
    def addEdge(self, label1, label2):
        """
        Add a new edge to the graph connecting two nodes

        Parameter
        ---------
            > label1,label2: the label of nodes that we want to connect
        """
        self.edges.append((label1,label2))



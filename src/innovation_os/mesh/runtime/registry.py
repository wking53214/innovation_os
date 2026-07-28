class NodeRegistry:


    def __init__(self):

        self.nodes = {}



    def register(
        self,
        node
    ):

        node.status = "online"

        self.nodes[
            node.node_id
        ] = node


        return node



    def get(
        self,
        node_id
    ):

        return self.nodes.get(
            node_id
        )

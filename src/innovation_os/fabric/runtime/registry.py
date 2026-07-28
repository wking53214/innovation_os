class FabricRegistry:


    def __init__(self):

        self.nodes = {}



    def register(
        self,
        node
    ):

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



    def list_nodes(
        self
    ):

        return list(
            self.nodes.values()
        )

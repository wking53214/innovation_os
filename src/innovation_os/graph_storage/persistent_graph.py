from src.innovation_os.storage.database import (
    InnovationDatabase,
)


class PersistentInnovationGraph:


    def __init__(
        self,
        database_path="innovation_graph.db",
    ):

        self.database = InnovationDatabase(
            database_path
        )


    def add_node(
        self,
        node_id,
        node_type,
        label,
    ):

        self.database.add_node(
            node_id,
            node_type,
            label,
        )


    def add_relationship(
        self,
        source_id,
        target_id,
        relationship,
    ):

        self.database.add_relationship(
            source_id,
            target_id,
            relationship,
        )


    def get_node(
        self,
        node_id,
    ):

        return self.database.get_node(
            node_id
        )


    def get_connections(
        self,
        node_id,
    ):

        return self.database.get_relationships(
            node_id
        )

import sqlite3
from pathlib import Path


class InnovationDatabase:

    def __init__(
        self,
        path="innovation_os.db",
    ):
        self.path = Path(path)
        self.connection = sqlite3.connect(
            self.path
        )

        self.initialize()


    def initialize(self):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS nodes (
                node_id TEXT PRIMARY KEY,
                node_type TEXT NOT NULL,
                label TEXT NOT NULL
            )
            """
        )

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS relationships (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                source_id TEXT NOT NULL,
                target_id TEXT NOT NULL,
                relationship TEXT NOT NULL
            )
            """
        )

        self.connection.commit()


    def add_node(
        self,
        node_id,
        node_type,
        label,
    ):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT OR REPLACE INTO nodes
            VALUES (?, ?, ?)
            """,
            (
                node_id,
                node_type,
                label,
            ),
        )

        self.connection.commit()


    def get_node(
        self,
        node_id,
    ):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM nodes
            WHERE node_id = ?
            """,
            (node_id,),
        )

        return cursor.fetchone()


    def add_relationship(
        self,
        source_id,
        target_id,
        relationship,
    ):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO relationships
            (
                source_id,
                target_id,
                relationship
            )
            VALUES (?, ?, ?)
            """,
            (
                source_id,
                target_id,
                relationship,
            ),
        )

        self.connection.commit()


    def get_relationships(
        self,
        node_id,
    ):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM relationships
            WHERE source_id = ?
            OR target_id = ?
            """,
            (
                node_id,
                node_id,
            ),
        )

        return cursor.fetchall()

from innovation_os.persistence import PersistenceStore


class RuntimeStateManager:


    def __init__(self):

        self.store = PersistenceStore()


    def set(
        self,
        key,
        value
    ):

        return self.store.save(
            key,
            value
        )


    def get(
        self,
        key
    ):

        return self.store.load(
            key
        )

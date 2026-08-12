from innovation_os.memory.innovation_memory import (
    InnovationMemory,
)


def test_memory_query():

    memory = InnovationMemory()


    result = memory.query(
        "Sentinel"
    )


    assert (
        result.query
        ==
        "Sentinel"
    )

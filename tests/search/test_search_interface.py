from src.innovation_os.search.interface import (
    InnovationSearch,
)



def test_search():

    search = InnovationSearch()


    search.index(
        "PROJECT-001",
        "PROJECT",
        "Sentinel AI Governance",
    )


    results = search.search(
        "governance"
    )


    assert len(results) == 1
    assert results[0].item_id == "PROJECT-001"

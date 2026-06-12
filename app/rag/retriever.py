import chromadb

client = chromadb.PersistentClient(
    path="data/chroma_db"
)

collection = client.get_collection(
    "waiverpro_rules"
)


def retrieve_rule(query, top_k=1):

    results = collection.query(
        query_texts=[query],
        n_results=top_k
    )

    return results


if __name__ == "__main__":

    result = retrieve_rule(
        "Facilities page filters and status tracking"
    )

    print(result)
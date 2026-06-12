import chromadb
import json

RULES_FILE = "data/guidelines/rules.json"

client = chromadb.PersistentClient(
    path="data/chroma_db"
)

collection = client.get_or_create_collection(
    name="waiverpro_rules"
)


def load_rules():

    with open(
        RULES_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)


def build_db():

    rules = load_rules()

    try:
        existing = collection.get()

        if existing["ids"]:
            collection.delete(
                ids=existing["ids"]
            )

    except Exception:
        pass

    for i, rule in enumerate(rules):

        collection.add(
            ids=[str(i)],
            documents=[rule["content"]],
            metadatas=[
                {
                    "title": rule["title"]
                }
            ]
        )

    print(
        f"Stored {len(rules)} rules"
    )


if __name__ == "__main__":
    build_db()
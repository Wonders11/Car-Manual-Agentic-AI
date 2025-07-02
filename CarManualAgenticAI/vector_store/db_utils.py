from langchain.vectorstores import AstraDB
from langchain.embeddings.openai import OpenAIEmbeddings

vector_store = AstraDB.from_existing_index(
    embedding=OpenAIEmbeddings(),
    collection_name="car_manuals"
)

def search_manual(company, model, fuel_type, query, k=3):
    filters = {
        "company": company,
        "model": model,
        "fuel_type": fuel_type
    }
    results = vector_store.similarity_search_with_score(query, k=k, filter=filters)
    return results

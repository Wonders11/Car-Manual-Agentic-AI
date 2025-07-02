from vector_store.db_utils import search_manual
from langgraph_app.llm_utils import run_rag_pipeline

def hyundai_agent(model, fuel_type, query):
    results = search_manual("Hyundai", model, fuel_type, query)
    return run_rag_pipeline(results, query)

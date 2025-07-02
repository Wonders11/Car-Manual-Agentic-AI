from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

llm = ChatOpenAI(model="gpt-4o")

def run_rag_pipeline(docs, query):
    if not docs:
        return "No relevant information found."

    context = "\n\n".join([doc.page_content for doc, _ in docs])

    prompt = f"""
    You are a car manual assistant. Use the following context to answer the question:

    Context:
    {context}

    Question:
    {query}

    Answer:
    """
    response = llm.invoke(prompt)
    return response.content

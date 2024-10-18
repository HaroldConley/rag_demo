import os
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings


class Embedder:
    def __init__(self):
        self.openai_api_key = os.environ.get("OPENAI_API_KEY")

        self.embeddings = OpenAIEmbeddings(
            model="text-embedding-3-small"
        )

    def create_vectorstore_for_list(self, texts_list: list):
        vectorstore = InMemoryVectorStore.from_texts(
            [text for text in texts_list],
            embedding=self.embeddings
        )
        return vectorstore

    def ask_vectorstore(self, query: str, vectorstore, number_of_results: int = 3) -> str:
        retrieved_documents = vectorstore.similarity_search(query, k=number_of_results)
        retrieved_chunks:list[str] = [retrieved_document.page_content for retrieved_document in retrieved_documents]
        return "\n\n".join(retrieved_chunks)


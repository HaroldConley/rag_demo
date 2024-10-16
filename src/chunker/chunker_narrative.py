from langchain_text_splitters import RecursiveCharacterTextSplitter


class ChunkerNarrative:
    def __init__(self, chunck_size=1000, chunk_overlap=200, length_function=len, is_separator_regex=False):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunck_size,
            chunk_overlap=chunk_overlap,
            length_function=length_function,
            is_separator_regex=is_separator_regex
        )

    def chunker_narrative(self, doc_path: str) -> list:
        with open(doc_path, encoding='utf-8') as f:
            document = f.read()

        chunks = self.text_splitter.create_documents([document])

        return chunks

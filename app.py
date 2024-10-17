import streamlit as st
from src.chunker.chunker_narrative import ChunkerNarrative
from src.embedder.embedder import Embedder

# Backend
chunker = ChunkerNarrative()
embedder = Embedder()


########################################
################## UI ##################
########################################
st.title("Chat with your document")

# Upload
### PUT A SIZE LIMIT TO IT (10Mb)
uploaded_file = st.file_uploader("Upload your file")
st.write(f"{type(uploaded_file)}")

if uploaded_file is not None:
    bytes_object = uploaded_file.read()

    # Convert the bytes object to str
    read_document = bytes_object.decode('utf-8')

    # Chunking
    chunks_as_documents = chunker.chunker_narrative(read_document)
    chunks_as_str = [chunk_as_documents.page_content for chunk_as_documents in chunks_as_documents]

    # Embedding and Vectorstoring
    vectorstore = embedder.create_vectorstore_for_list(chunks_as_str)


# Doc type selection
doc_type = st.radio(
    "Document type",
    ["Narrative or textual", "Technical or legal", "Scientific or research papers"],
    captions=[
        "Document with plain text mostly, such as articles, long reports, stories",
        "Document with clear structures such as clauses, numbered lists or tables",
        "Document with sections such as introduction, methodology, results and discussion",
    ],
)

if doc_type == "Narrative or textual":
    temp = 1
else:
    temp = 2


# Query
query = st.text_area(
    "What would you like to know?"
)

# Answer
if st.button("Send"):
    answer = embedder.ask_vectorstore(query, vectorstore, 2)
    st.write(answer)


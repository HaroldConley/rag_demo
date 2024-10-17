import streamlit as st
from src.chunker.chunker_narrative import ChunkerNarrative

# Backend
chunker = ChunkerNarrative()


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
    chunks = chunker.chunker_narrative(read_document)


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
txt = st.text_area(
    "What would you like to know?"
)

# Answer
if st.button("Send"):
    st.write(f"")


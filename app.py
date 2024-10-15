import streamlit as st
import pandas as pd
from io import StringIO


# UI
st.title("Chat with your document")

# Upload
uploaded_file = st.file_uploader("Upload your file")

if uploaded_file is not None:
    bytes_data = uploaded_file.read()


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
    st.write(f"Answer HERE")


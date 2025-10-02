from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_documents(docs, chunk_size=500, chunk_overlap=50):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    new_docs = []
    for d in docs:
        chunks = splitter.split_text(d["content"])
        for idx, chunk in enumerate(chunks):
            new_docs.append({
                "path": d["path"],
                "content": chunk,
                "chunk_id": idx
            })
    return new_docs

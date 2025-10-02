from langchain.vectorstores import Chroma

def build_vectordb(docs, embedder, persist_dir="chroma_db"):
    texts = [d["content"] for d in docs]
    metadatas = [{"path": d["path"], "chunk_id": d.get("chunk_id", 0)} for d in docs]
    vectordb = Chroma.from_texts(texts, embedder, metadatas=metadatas, persist_directory=persist_dir)
    return vectordb

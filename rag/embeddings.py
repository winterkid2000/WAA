from sentence_transformers import SentenceTransformer

def get_embedder(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"):
    return SentenceTransformer(model_name)

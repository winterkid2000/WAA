def search_docs(vectordb, query, k=3):
    results = vectordb.similarity_search(query, k=k)
    return results

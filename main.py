# main.py
from rag.loader import load_documents
from rag.splitter import split_documents
from rag.embeddings import get_embedder
from rag.vectordb import build_vectordb
from rag.retriever import search_docs

def main():
    # 1. 문서 로드
    docs = load_documents("data")
    print(f"{len(docs)}개의 문서를 불러왔습니다.")

    # 2. 분할
    split_docs = split_documents(docs)

    # 3. 임베딩 & VectorDB 구축
    embedder = get_embedder()
    vectordb = build_vectordb(split_docs, embedder)

    # 4. 검색 테스트
    query = "정기 회의록 작성"
    results = search_docs(vectordb, query)
    print("\n 유사 문서 검색 결과:")
    for r in results:
        print(r.page_content[:100], "...", r.metadata)

if __name__ == "__main__":
    main()

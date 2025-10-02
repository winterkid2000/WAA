# schema/extractor.py
import json
import re

def extract_schema(llm, sample_doc: str) -> dict:
    """
    LLM을 사용하여 문서 스키마(JSON 필드 목록)를 추출합니다.
    
    Args:
        llm: HuggingFace pipeline (text-generation)
        sample_doc: 회의록 원문 텍스트
    
    Returns:
        dict: {"문서종류": ..., "필수항목": [...]}
    """
    prompt = f"""
    너는 행정 문서 분석 AI이다. 아래 문서를 보고,
    이 문서를 작성하기 위해 반드시 필요한 항목을 JSON 형식으로 추출하라.

    문서 예시:
    {sample_doc}

    출력 예시:
    {{
      "문서종류": "회의록",
      "필수항목": ["날짜", "장소", "참석자", "안건", "결론"]
    }}
    """

    raw = llm(prompt)[0]["generated_text"]

    # JSON 추출 (LLM 출력에서 불필요한 텍스트 제거)
    try:
        match = re.search(r"\{.*\}", raw, re.S)
        if match:
            schema = json.loads(match.group())
        else:
            schema = {"문서종류": "회의록", "필수항목": []}
    except Exception as e:
        print(f"[WARN] JSON 파싱 실패: {e}")
        schema = {"문서종류": "회의록", "필수항목": []}

    return schema

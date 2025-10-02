# schema/manager.py

class SchemaManager:
    def __init__(self, schema: dict):
        """
        Args:
            schema (dict): {"문서종류": "회의록", "필수항목": ["날짜", "장소", "참석자", ...]}
        """
        self.schema = schema
        self.fields = schema.get("필수항목", [])
        self.collected = {}
        self.current_idx = 0

    def has_next(self) -> bool:
        """아직 질문할 필드가 남아있는지 확인"""
        return self.current_idx < len(self.fields)

    def next_question(self) -> str:
        """다음 질문을 생성"""
        if not self.has_next():
            return None
        field = self.fields[self.current_idx]
        return f"{field}을(를) 알려주세요."

    def record_answer(self, answer: str):
        """사용자 답변 기록"""
        field = self.fields[self.current_idx]
        self.collected[field] = answer
        self.current_idx += 1

    def get_result(self) -> dict:
        """최종 수집된 데이터 반환"""
        return {
            "문서종류": self.schema.get("문서종류", "회의록"),
            "필드값": self.collected
        }

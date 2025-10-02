import os
import olefile

def load_hwp_text(filepath):
    if not olefile.isOleFile(filepath):
        raise ValueError("올바른 HWP 파일이 아닙니다.")
    f = olefile.OleFileIO(filepath)
    encoded_text = f.openstream("PrvText").read()
    return encoded_text.decode("utf-16")  # HWP 내부 텍스트 스트림 추출

def load_documents(base_path="data"):
    docs = []
    for folder, _, files in os.walk(base_path):
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            full_path = os.path.join(folder, f)

            if ext == ".txt":
                with open(full_path, "r", encoding="utf-8") as file:
                    content = file.read()
            elif ext == ".hwp":
                try:
                    content = load_hwp_text(full_path)
                except Exception as e:
                    print(f"[WARN] {f} 처리 실패: {e}")
                    continue
            else:
                continue

            docs.append({
                "path": full_path,
                "content": content
            })
    return docs

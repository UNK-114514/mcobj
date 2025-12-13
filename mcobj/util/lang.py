import json


class Lang:
    def __init__(self, lang: str = "zh_cn"):
        self.file_path = f"../resources/lang/{lang}.json"

    def get_content(self):
        with open(self.file_path, "r", encoding="utf-8") as f:
            content = json.load(f)
        return content
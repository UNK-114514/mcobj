import json


class Config:
    def __init__(self, config_path):
        self.config_path = config_path
    def get_content(self):
        with open(self.config_path, "r", encoding="utf-8") as f:
            content = json.load(f)
        return content
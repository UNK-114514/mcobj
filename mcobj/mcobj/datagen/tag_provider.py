import json

from mcobj.datagen.provider import Provider
from mcobj.obj.identifier import Identifier


class TagProvider(Provider):
    def __init__(self, identifier: Identifier):
        super().__init__(identifier)
        self.value = {"replace": False, "values": []}

    def get_name(self) -> str:
        return "TagProvider"

    def generate(self) -> str:
        return json.dumps(self.value)

    def store(self, output_file_path) -> bool:
        try:
            with open(output_file_path, "r", encoding="utf-8") as f:
                f.write(self.generate())

        except Exception as e:
            print(f"Error [at TagProvider.generate / writing file]: {e}")
            return False

        return True

    def add_item(self, item):
        self.value["values"].append(item.identifier.to_string())
        return self

    def add_obj(self, obj: object):
        self.value["values"].append(str(obj))
        return self

    def replace(self, replace: bool = False):
        self.value["replace"] = replace
        return self
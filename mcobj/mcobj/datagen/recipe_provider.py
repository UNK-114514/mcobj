import json

from mcobj.datagen.provider import Provider
from mcobj.obj.identifier import Identifier
from mcobj.obj.item import Item


class CraftingShapedRecipeProvider(Provider):
    def __init__(self, identifier: Identifier):
        super().__init__(identifier)
        self.value = {"type": "crafting_shaped", "key": {}, "pattern": [], "result": {}}

    def get_name(self) -> str:
        return "CraftingShapedRecipeProvider"

    def generate(self) -> str:
        return json.dumps(self.value)

    def store(self, output_file_path) -> bool:
        try:
            with open(output_file_path, "r", encoding="utf-8") as f:
                f.write(self.generate())

        except Exception as e:
            print(f"Error [at CraftingShapedRecipeProvider.generate / writing file]: {e}")
            return False

        return True

    def pattern(self, patten: list[str]):
        self.value["pattern"] = patten
        return self

    def result(self, item: str | dict | Item):
        if isinstance(item, str):
            self.value["result"]["id"] = item

        elif isinstance(item, dict):
            self.value["result"] = item

        elif isinstance(item, Item):
            self.value["result"]["id"] = item.identifier.to_string()
            if item.components:
                self.value["result"]["components"] = item.components

        return self

    def group(self, group: str):
        self.value["group"] = group

    def category(self, category: str):
        self.value["category"] = category

    def add_key(self, key: str, value: str | Item):
        if isinstance(value, str):
            self.value["key"][key] = value

        elif isinstance(value, Item):
            self.value["key"][key] = value.identifier.to_string()
        return self
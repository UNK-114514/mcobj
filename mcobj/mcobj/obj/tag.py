import json

from mcobj.mc_object import McObject
from mcobj.obj.identifier import Identifier


class Tag(McObject):
    def __init__(self, identifier: Identifier):
        super().__init__(identifier)
        self.value = ""

    def __str__(self) -> str:
        return self.to_string()

    def to_string(self) -> str:
        return "#" + self.identifier.namespace + ":" + self.identifier.path

    def load(self, path: str):
        with open(path, "r", encoding="utf-8") as f:
            self.value = json.load(f)
        return self
from mcobj.mc_object import McObject
from mcobj.obj.identifier import Identifier


class Item(McObject):
    def __init__(self, identifier: Identifier, components: dict = None):
        super().__init__(identifier)
        self.components = components

    def __str__(self) -> str:
        return self.to_string()

    def to_string(self) -> str:
        return self.identifier.to_string()
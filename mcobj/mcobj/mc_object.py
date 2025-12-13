from mcobj.obj.identifier import Identifier


class McObject:
    def __init__(self, identifier: Identifier):
        self.identifier = identifier

    def __str__(self) -> str:
        pass

    def to_string(self) -> str:
        pass
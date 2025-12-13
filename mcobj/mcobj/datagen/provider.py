from mcobj.obj.identifier import Identifier


class Provider:
    def __init__(self, identifier: Identifier):
        self.identifier = identifier

    def get_name(self) -> str:
        return "Provider"

    def generate(self) -> str:
        pass

    def store(self, output_file_path) -> bool:
        pass
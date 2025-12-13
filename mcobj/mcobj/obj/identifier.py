class Identifier:
    def __init__(self, namespace, path):
        self.namespace = namespace
        self.path = path

    def __str__(self) -> str:
        return self.to_string()

    def to_string(self):
        return self.namespace + ":" + self.path


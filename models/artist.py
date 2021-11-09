class Artist:
    def __init__(self, name, id=None):
        self.name = name
        self.id = id

    def __repr__(self):
        return f"{self.name}"
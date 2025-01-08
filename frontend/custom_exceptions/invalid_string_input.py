class InvalidStringInput(Exception):
    def __init__(self, message):
        self.message = f"(Invalid String Input): {message}"
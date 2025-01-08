class InvalidNumberInput(Exception):
    def __init__(self, message):
        self.message = f"(Invalid Number Input): {message}"
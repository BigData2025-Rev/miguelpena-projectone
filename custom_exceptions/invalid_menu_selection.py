class InvalidMenuSelection(Exception):
    def __init__(self, message):
        self.message = f"(Invalid Menu Selection): {message}"
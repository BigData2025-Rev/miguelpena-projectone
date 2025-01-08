class InvalidLoginCredentials(Exception):
    def __init__(self, message):
        self.message = f"(Invalid Login Credentials): {message}"
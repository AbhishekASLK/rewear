class SessionManager:
    def __init__(self, request):
        self.session = request.session

    def get(self, key: str, default=None):
        return self.session.get(key, default)

    def set(self, key: str, value):
        self.session[key] = value

    def pop(self, key: str, default=None):
        return self.session.pop(key, default)

    def exists(self, key: str) -> bool:
        return key in self.session

  

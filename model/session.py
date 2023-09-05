from model.user import User

class Session:
    def __init__(self):
        self.user = None
    
    def set_user(self, user: User):
        self.user = user
    
    def is_user_logged_in(self) -> bool:
        return self.user != 0
    
    def get_user(self) -> int:
        return self.user

    def log_user_out(self) -> None:
        self.user = None
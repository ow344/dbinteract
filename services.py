from config import session
from models import User

class UserService:
    def __init__(self):
        pass

    def get_user(self, id):
        return session.get(User, id)

    def get_users(self):
        return session.query(User).all()

    def add_user(self, user):
        session.add(user)
        session.commit()

    def update_user(self, user):
        session.merge(user)
        session.commit()

    def delete_user(self, id):
        session.delete(self.get_user(id))
        session.commit()



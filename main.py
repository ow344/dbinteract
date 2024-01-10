from services import UserService

if __name__ == "__main__":
    user_service = UserService()
    users = user_service.get_users()
    for user in users:
        print(user)
